import pygame
import random
from .settings import *
from .entities import Player, Meteor, Crystal
from .utils import load_highscore, save_highscore

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
        self.highscore = load_highscore()
        self.reset()

    def reset(self):
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        self.crystals = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        self.score = 0
        self.lives = 3
        self.spawn_timer = 0
        self.game_over = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            if not self.game_over:
                self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.all_sprites.update()
        
        self.spawn_timer += 1
        # Spawn de meteoros
        if self.spawn_timer % SPAWN_RATE_METEOR == 0:
            m = Meteor()
            self.all_sprites.add(m)
            self.meteors.add(m)
            
        # Spawn de cristais (mais raros)
        if self.spawn_timer % SPAWN_RATE_CRYSTAL == 0:
            c = Crystal()
            self.all_sprites.add(c)
            self.crystals.add(c)
            
        # Colisão com meteoros
        hits = pygame.sprite.spritecollide(self.player, self.meteors, True, pygame.sprite.collide_mask)
        for hit in hits:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True
                if self.score > self.highscore:
                    self.highscore = self.score
                    save_highscore(self.highscore)
        
        # Coleta de cristais
        collections = pygame.sprite.spritecollide(self.player, self.crystals, True)
        for crystal in collections:
            self.score += 50
            
        # Pontuação por tempo
        if self.spawn_timer % 60 == 0:
            self.score += 1

    def draw(self):
        self.screen.fill(BLACK)
        try:
            bg = pygame.image.load(BACKGROUND_IMG).convert()
            for x in range(0, WIDTH, bg.get_width()):
                for y in range(0, HEIGHT, bg.get_height()):
                    self.screen.blit(bg, (x, y))
        except: pass
            
        self.all_sprites.draw(self.screen)
        
        # HUD
        draw_text(self.screen, f"Pontos: {self.score}", 20, WIDTH // 2, 10)
        draw_text(self.screen, f"Vidas: {self.lives}", 20, 60, 10, RED)
        draw_text(self.screen, f"Recorde: {self.highscore}", 16, WIDTH - 80, 10, YELLOW)
        
        if self.game_over:
            self.screen.fill((0, 0, 0, 150), special_flags=pygame.BLEND_RGBA_MULT)
            draw_text(self.screen, "GAME OVER", 64, WIDTH // 2, HEIGHT // 3, RED)
            draw_text(self.screen, f"Pontuação Final: {self.score}", 32, WIDTH // 2, HEIGHT // 2)
            draw_text(self.screen, "Pressione R para reiniciar ou ESC para sair", 20, WIDTH // 2, HEIGHT * 2 // 3)
            
        pygame.display.flip()
