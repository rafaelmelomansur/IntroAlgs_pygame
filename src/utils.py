import os
from .settings import ARQUIVO_RECORDE, ARQUIVO_RANKING

# ──────────────────────────────────────────────
# Funções de Recorde
# ──────────────────────────────────────────────

def carregar_recorde():
    """Lê o recorde do arquivo data/highscore.txt.
    Retorna 0 se o arquivo não existir ou contiver valor inválido.
    """
    if not os.path.exists(ARQUIVO_RECORDE):
        os.makedirs(os.path.dirname(ARQUIVO_RECORDE), exist_ok=True)
        with open(ARQUIVO_RECORDE, "w") as arquivo:
            arquivo.write("0")
        return 0
    try:
        with open(ARQUIVO_RECORDE, "r") as arquivo:
            conteudo = arquivo.read().strip()
            return int(conteudo) if conteudo else 0
    except (ValueError, IOError):
        return 0


def salvar_recorde(pontuacao):
    """Salva a pontuação como novo recorde apenas se ela for maior que o atual.
    Retorna True se o recorde foi atualizado, False caso contrário.
    """
    recorde_atual = carregar_recorde()
    if pontuacao > recorde_atual:
        try:
            with open(ARQUIVO_RECORDE, "w") as arquivo:
                arquivo.write(str(pontuacao))
            return True
        except IOError:
            return False
    return False


# ──────────────────────────────────────────────
# Funções de Ranking
# ──────────────────────────────────────────────

TAMANHO_MAXIMO_RANKING = 5   # Número máximo de entradas no ranking


def carregar_ranking():
    """Lê o ranking do arquivo data/ranking.txt.
    Retorna uma lista de inteiros ordenada do maior para o menor.
    """
    if not os.path.exists(ARQUIVO_RANKING):
        return []
    pontuacoes = []
    try:
        with open(ARQUIVO_RANKING, "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    pontuacoes.append(int(linha))
    except IOError:
        pass
    return sorted(pontuacoes, reverse=True)


def salvar_ranking(pontuacao):
    """Adiciona a pontuação ao ranking e mantém apenas os top-5.
    Retorna a lista atualizada do ranking.
    """
    pontuacoes = carregar_ranking()
    pontuacoes.append(pontuacao)
    pontuacoes = sorted(pontuacoes, reverse=True)[:TAMANHO_MAXIMO_RANKING]
    try:
        os.makedirs(os.path.dirname(ARQUIVO_RANKING), exist_ok=True)
        with open(ARQUIVO_RANKING, "w") as arquivo:
            for p in pontuacoes:
                arquivo.write(str(p) + "\n")
    except IOError:
        pass
    return pontuacoes


# ──────────────────────────────────────────────
# Compatibilidade com importações antigas
# ──────────────────────────────────────────────

def load_highscore():
    """Alias de compatibilidade para carregar_recorde()."""
    return carregar_recorde()


def save_highscore(pontuacao):
    """Alias de compatibilidade para salvar_recorde()."""
    return salvar_recorde(pontuacao)


# ──────────────────────────────────────────────
# Utilitário de renderização de texto
# ──────────────────────────────────────────────

def desenhar_texto(superficie, texto, tamanho, x, y, cor=(255, 255, 255)):
    """Desenha texto centralizado horizontalmente na posição (x, y)."""
    import pygame
    nome_fonte = pygame.font.match_font('arial')
    fonte = pygame.font.Font(nome_fonte, tamanho)
    superficie_texto = fonte.render(texto, True, cor)
    retangulo_texto = superficie_texto.get_rect()
    retangulo_texto.midtop = (x, y)
    superficie.blit(superficie_texto, retangulo_texto)
