import pygame
import sys
from .settings import *
from .entities import Player, Meteor

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.reset()

    def reset(self):
        """Inicializa ou reinicia os elementos do protótipo."""
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        self.score = 0
        self.spawn_timer = 0

    def run(self):
        """Loop principal do jogo."""
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()
        
        # Spawn de meteoros (elemento interativo)
        self.spawn_timer += 1
        if self.spawn_timer >= SPAWN_RATE_METEOR:
            m = Meteor()
            self.all_sprites.add(m)
            self.meteors.add(m)
            self.spawn_timer = 0
            
        # Detecção de colisão simples (requisito do protótipo)
        hits = pygame.sprite.spritecollide(self.player, self.meteors, True)
        if hits:
            print("Colisão detectada!")
            self.score -= 10 # Penalidade simples para o protótipo

    def draw(self):
        self.screen.fill(BLACK)
        
        # Desenha fundo se disponível
        try:
            bg = pygame.image.load(BACKGROUND_IMG).convert()
            for x in range(0, WIDTH, bg.get_width()):
                for y in range(0, HEIGHT, bg.get_height()):
                    self.screen.blit(bg, (x, y))
        except:
            pass
            
        self.all_sprites.draw(self.screen)
        
        # HUD simples para o protótipo
        draw_text(self.screen, f"Pontos: {self.score}", 24, WIDTH // 2, 20)
        draw_text(self.screen, "PROTÓTIPO - SEMANA 2", 14, WIDTH // 2, HEIGHT - 20, (150, 150, 150))
        
        pygame.display.flip()
