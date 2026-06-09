import pygame

# Configurações da Janela
WIDTH = 800
HEIGHT = 600
FPS = 60
TITLE = "Aventura Galáctica: Defesa Estelar"

# Cores (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Configurações do Jogo
PLAYER_SPEED = 7
METEOR_MIN_SPEED = 3
METEOR_MAX_SPEED = 8
CRYSTAL_SPEED = 5
SPAWN_RATE_METEOR = 30  # Frames entre cada spawn inicial
SPAWN_RATE_CRYSTAL = 300 # Cristais são mais raros

# Caminhos de Arquivos
DATA_FILE = "data/highscore.txt"

# Assets
ASSETS_PATH = "assets/kenney_space_shooter/PNG"
PLAYER_IMG = ASSETS_PATH + "/playerShip1_blue.png"
METEOR_IMG = ASSETS_PATH + "/Meteors/meteorBrown_big1.png"
CRYSTAL_IMG = ASSETS_PATH + "/Power-ups/powerupYellow_star.png"
BACKGROUND_IMG = ASSETS_PATH + "/Backgrounds/black.png"

