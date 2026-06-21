import pygame

# Configurações da Janela
LARGURA = 800
ALTURA = 600
FPS = 60
TITULO = "Aventura Galáctica: Defesa Estelar"

# Cores (RGB)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CINZA_ESCURO = (30, 30, 30)

# Configurações do Jogador
VELOCIDADE_JOGADOR = 7

# Configurações dos Meteoros
VELOCIDADE_METEORO_MIN = 3
VELOCIDADE_METEORO_MAX = 8

# Configurações dos Cristais
VELOCIDADE_CRISTAL = 5

# Taxa de geração de objetos (em frames)
TAXA_SPAWN_METEORO = 30    # Frames entre cada spawn de meteoro
TAXA_SPAWN_CRISTAL = 300   # Cristais são mais raros

# Pontuação
PONTOS_CRISTAL = 50        # Pontos ganhos ao coletar um cristal
PONTOS_TEMPO = 1           # Pontos ganhos a cada 60 frames (1 segundo)

# Vidas iniciais do jogador
VIDAS_INICIAIS = 3

# Caminhos de Arquivos
ARQUIVO_RECORDE = "data/highscore.txt"
ARQUIVO_RANKING = "data/ranking.txt"

# Compatibilidade: mantém o nome DATA_FILE para não quebrar importações existentes
DATA_FILE = ARQUIVO_RECORDE

# Assets
CAMINHO_ASSETS = "assets/kenney_space_shooter/PNG"
IMAGEM_JOGADOR = CAMINHO_ASSETS + "/playerShip1_blue.png"
IMAGEM_METEORO = CAMINHO_ASSETS + "/Meteors/meteorBrown_big1.png"
IMAGEM_CRISTAL = CAMINHO_ASSETS + "/Power-ups/powerupYellow_star.png"
IMAGEM_FUNDO   = CAMINHO_ASSETS + "/Backgrounds/black.png"
