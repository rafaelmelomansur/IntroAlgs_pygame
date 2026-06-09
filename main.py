import sys
from src.engine import Game

def main():
    """Ponto de entrada principal do jogo."""
    g = Game()
    g.show_start_screen()
    
    while g.running:
        g.new()
        g.show_go_screen()
    
    sys.exit()

if __name__ == "__main__":
    main()
