import sys
from src.engine import Jogo


def principal():
    """Ponto de entrada principal do jogo."""
    jogo = Jogo()
    jogo.show_start_screen()

    while jogo.rodando:
        jogo.new()
        jogo.show_go_screen()

    sys.exit()


if __name__ == "__main__":
    principal()
