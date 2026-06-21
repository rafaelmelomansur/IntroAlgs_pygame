import pygame
import random
from .settings import *


def carregar_imagem(caminho, escala=None):
    """Carrega uma imagem do disco. Retorna um quadrado magenta em caso de erro."""
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        if escala:
            imagem = pygame.transform.scale(imagem, escala)
        return imagem
    except Exception:
        superficie = pygame.Surface((50, 50))
        superficie.fill((255, 0, 255))
        return superficie


class Jogador(pygame.sprite.Sprite):
    """Nave espacial controlada pelo jogador."""

    def __init__(self):
        super().__init__()
        self.image = carregar_imagem(IMAGEM_JOGADOR, (50, 38))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 10
        self.velocidade_x = 0

    def update(self):
        self.velocidade_x = 0
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.velocidade_x = -VELOCIDADE_JOGADOR
        if teclas[pygame.K_RIGHT]:
            self.velocidade_x = VELOCIDADE_JOGADOR
        self.rect.x += self.velocidade_x
        # Mantém a nave dentro dos limites horizontais da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA


class Meteoro(pygame.sprite.Sprite):
    """Meteoro que cai do topo da tela em velocidade aleatória."""

    def __init__(self, multiplicador_velocidade=1.0):
        super().__init__()
        tamanho = random.randint(30, 70)
        self.image = carregar_imagem(IMAGEM_METEORO, (tamanho, tamanho))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = random.randrange(LARGURA - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        velocidade_base = random.randrange(VELOCIDADE_METEORO_MIN, VELOCIDADE_METEORO_MAX)
        self.velocidade_y = int(velocidade_base * multiplicador_velocidade)

    def update(self):
        self.rect.y += self.velocidade_y
        # Remove o sprite quando sai da tela pela parte inferior
        if self.rect.top > ALTURA + 10:
            self.kill()


class Cristal(pygame.sprite.Sprite):
    """Cristal de energia que cai do topo e pode ser coletado para ganhar pontos."""

    def __init__(self):
        super().__init__()
        self.image = carregar_imagem(IMAGEM_CRISTAL, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(LARGURA - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidade_y = VELOCIDADE_CRISTAL

    def update(self):
        self.rect.y += self.velocidade_y
        # Remove o sprite quando sai da tela pela parte inferior
        if self.rect.top > ALTURA + 10:
            self.kill()
