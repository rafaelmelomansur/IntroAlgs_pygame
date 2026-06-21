import pygame
import sys
from .settings import *
from .entities import Jogador, Meteoro, Cristal
from .utils import carregar_recorde, salvar_recorde, salvar_ranking, carregar_ranking, desenhar_texto


class Jogo:
    """Classe principal que gerencia o loop do jogo, estados e eventos."""

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.recorde = carregar_recorde()

    # ──────────────────────────────────────────────
    # Inicialização de uma nova partida
    # ──────────────────────────────────────────────

    def new(self):
        """Prepara e inicia uma nova partida."""
        self.todos_sprites = pygame.sprite.Group()
        self.meteoros = pygame.sprite.Group()
        self.cristais = pygame.sprite.Group()

        self.jogador = Jogador()
        self.todos_sprites.add(self.jogador)

        self.pontuacao = 0
        self.vidas = VIDAS_INICIAIS
        self.contador_frames = 0
        self.nivel_dificuldade = 1
        self.fim_de_jogo = False

        self.executar()

    # ──────────────────────────────────────────────
    # Loop principal da partida
    # ──────────────────────────────────────────────

    def executar(self):
        """Loop principal: processa eventos, atualiza estado e renderiza."""
        while self.rodando:
            self.relogio.tick(FPS)
            self.processar_eventos()
            if not self.fim_de_jogo:
                self.atualizar()
            self.desenhar()

    # ──────────────────────────────────────────────
    # Processamento de eventos
    # ──────────────────────────────────────────────

    def processar_eventos(self):
        """Lê e trata todos os eventos do Pygame."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if self.fim_de_jogo:
                    if evento.key == pygame.K_r:
                        # Reinicia a partida sem sair do loop externo
                        self.new()
                    elif evento.key == pygame.K_ESCAPE:
                        self.rodando = False
                        pygame.quit()
                        sys.exit()

    # ──────────────────────────────────────────────
    # Atualização do estado do jogo
    # ──────────────────────────────────────────────

    def atualizar(self):
        """Atualiza sprites, gera objetos, verifica colisões e pontuação."""
        self.todos_sprites.update()
        self.contador_frames += 1

        # Aumenta a dificuldade a cada 30 segundos (1800 frames a 60 FPS)
        self.nivel_dificuldade = 1 + self.contador_frames // 1800

        # Multiplicador de velocidade dos meteoros conforme o nível
        multiplicador = 1.0 + (self.nivel_dificuldade - 1) * 0.2

        # Taxa de spawn diminui conforme o nível (mais meteoros)
        taxa_spawn_atual = max(10, TAXA_SPAWN_METEORO - (self.nivel_dificuldade - 1) * 5)

        # Geração de meteoros
        if self.contador_frames % taxa_spawn_atual == 0:
            meteoro = Meteoro(multiplicador_velocidade=multiplicador)
            self.todos_sprites.add(meteoro)
            self.meteoros.add(meteoro)

        # Geração de cristais (mais raros)
        if self.contador_frames % TAXA_SPAWN_CRISTAL == 0:
            cristal = Cristal()
            self.todos_sprites.add(cristal)
            self.cristais.add(cristal)

        # Colisão da nave com meteoros (com máscara de pixel)
        colisoes_meteoro = pygame.sprite.spritecollide(
            self.jogador, self.meteoros, True, pygame.sprite.collide_mask
        )
        for _ in colisoes_meteoro:
            self.vidas -= 1
            if self.vidas <= 0:
                self._encerrar_partida()
                return

        # Coleta de cristais
        colisoes_cristal = pygame.sprite.spritecollide(
            self.jogador, self.cristais, True
        )
        for _ in colisoes_cristal:
            self.pontuacao += PONTOS_CRISTAL

        # Pontuação por tempo de sobrevivência (1 ponto por segundo)
        if self.contador_frames % 60 == 0:
            self.pontuacao += PONTOS_TEMPO

    def _encerrar_partida(self):
        """Registra fim de jogo, salva recorde e ranking."""
        self.fim_de_jogo = True
        if self.pontuacao > self.recorde:
            self.recorde = self.pontuacao
            salvar_recorde(self.recorde)
        salvar_ranking(self.pontuacao)

    # ──────────────────────────────────────────────
    # Renderização
    # ──────────────────────────────────────────────

    def desenhar(self):
        """Renderiza todos os elementos na tela."""
        # Fundo
        self.tela.fill(PRETO)
        try:
            fundo = pygame.image.load(IMAGEM_FUNDO).convert()
            for x in range(0, LARGURA, fundo.get_width()):
                for y in range(0, ALTURA, fundo.get_height()):
                    self.tela.blit(fundo, (x, y))
        except Exception:
            pass

        self.todos_sprites.draw(self.tela)

        # HUD — informações do jogo
        desenhar_texto(self.tela, f"Pontos: {self.pontuacao}", 20, LARGURA // 2, 10, BRANCO)
        desenhar_texto(self.tela, f"Vidas: {self.vidas}", 20, 60, 10, VERMELHO)
        desenhar_texto(self.tela, f"Recorde: {self.recorde}", 16, LARGURA - 80, 10, AMARELO)
        desenhar_texto(self.tela, f"Nível: {self.nivel_dificuldade}", 16, LARGURA - 80, 30, VERDE)

        # Tela de fim de jogo
        if self.fim_de_jogo:
            sobreposicao = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            sobreposicao.fill((0, 0, 0, 160))
            self.tela.blit(sobreposicao, (0, 0))
            desenhar_texto(self.tela, "FIM DE JOGO", 64, LARGURA // 2, ALTURA // 4, VERMELHO)
            desenhar_texto(self.tela, f"Pontuação Final: {self.pontuacao}", 32, LARGURA // 2, ALTURA // 2 - 30, BRANCO)
            if self.pontuacao == self.recorde and self.pontuacao > 0:
                desenhar_texto(self.tela, "Novo Recorde!", 28, LARGURA // 2, ALTURA // 2 + 20, AMARELO)
            desenhar_texto(
                self.tela,
                "Pressione R para reiniciar  |  ESC para sair",
                20, LARGURA // 2, ALTURA * 2 // 3 + 20, BRANCO
            )
            # Exibe ranking
            ranking = carregar_ranking()
            if ranking:
                desenhar_texto(self.tela, "Top 5:", 18, LARGURA // 2, ALTURA * 2 // 3 + 60, AMARELO)
                for posicao, pts in enumerate(ranking, start=1):
                    desenhar_texto(
                        self.tela,
                        f"{posicao}. {pts} pts",
                        16, LARGURA // 2, ALTURA * 2 // 3 + 60 + posicao * 22, BRANCO
                    )

        pygame.display.flip()

    # ──────────────────────────────────────────────
    # Telas de início e encerramento
    # ──────────────────────────────────────────────

    def show_start_screen(self):
        """Exibe a tela de início e aguarda o jogador pressionar uma tecla."""
        self.tela.fill(PRETO)
        desenhar_texto(self.tela, TITULO, 36, LARGURA // 2, ALTURA // 4, AMARELO)
        desenhar_texto(self.tela, "Desvie dos meteoros e colete cristais!", 22, LARGURA // 2, ALTURA // 2 - 40, BRANCO)
        desenhar_texto(self.tela, "← → para mover a nave", 20, LARGURA // 2, ALTURA // 2, BRANCO)
        desenhar_texto(self.tela, "R: reiniciar  |  ESC: sair", 18, LARGURA // 2, ALTURA // 2 + 30, BRANCO)
        desenhar_texto(self.tela, f"Recorde atual: {self.recorde}", 20, LARGURA // 2, ALTURA * 2 // 3, AMARELO)
        desenhar_texto(self.tela, "Pressione qualquer tecla para começar", 22, LARGURA // 2, ALTURA * 3 // 4, VERDE)
        pygame.display.flip()
        self._aguardar_tecla()

    def show_go_screen(self):
        """Exibe a tela de 'jogue novamente' e aguarda decisão do jogador."""
        if not self.rodando:
            return
        self.tela.fill(PRETO)
        desenhar_texto(self.tela, "Jogar novamente?", 48, LARGURA // 2, ALTURA // 3, AMARELO)
        desenhar_texto(self.tela, "Pressione qualquer tecla para continuar", 22, LARGURA // 2, ALTURA // 2, BRANCO)
        desenhar_texto(self.tela, "ESC para sair", 18, LARGURA // 2, ALTURA // 2 + 40, VERMELHO)
        pygame.display.flip()
        self._aguardar_tecla()

    def _aguardar_tecla(self):
        """Pausa a execução até o jogador pressionar uma tecla."""
        aguardando = True
        while aguardando:
            self.relogio.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    aguardando = False
                    self.rodando = False
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        aguardando = False
                        self.rodando = False
                        pygame.quit()
                        sys.exit()
                    else:
                        aguardando = False


# Alias de compatibilidade para o main.py existente
Game = Jogo
