import os
from .settings import DATA_FILE

def load_highscore():
    """Lê o recorde do arquivo data/highscore.txt."""
    if not os.path.exists(DATA_FILE):
        # Garante que a pasta data existe
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            f.write("0")
        return 0
    
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            return int(content) if content else 0
    except (ValueError, IOError):
        return 0

def save_highscore(score):
    """Salva o novo recorde se ele for maior que o atual."""
    current_high = load_highscore()
    if score > current_high:
        try:
            with open(DATA_FILE, "w") as f:
                f.write(str(score))
            return True
        except IOError:
            return False
    return False

def draw_text(surface, text, size, x, y, color=(255, 255, 255)):
    """Função auxiliar para desenhar texto na tela."""
    import pygame
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
