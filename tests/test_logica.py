"""
Testes das funções de lógica pura do jogo (src/funcoes.py).
Estas funções não dependem do Pygame e podem ser executadas sem display.
"""
import pytest
from src.funcoes import (
    calcular_pontos,
    tomar_dano,
    jogador_perdeu,
    limitar_valor,
    calcular_nivel,
    calcular_taxa_spawn,
)


# ──────────────────────────────────────────────
# calcular_pontos
# ──────────────────────────────────────────────

def test_calcular_pontos_soma_correta():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_com_zero():
    """Deve retornar o valor atual quando os pontos ganhos são zero."""
    assert calcular_pontos(100, 0) == 100


def test_calcular_pontos_acumulativo():
    """Deve acumular pontos em chamadas sucessivas."""
    pontuacao = 0
    pontuacao = calcular_pontos(pontuacao, 50)
    pontuacao = calcular_pontos(pontuacao, 50)
    assert pontuacao == 100


# ──────────────────────────────────────────────
# tomar_dano
# ──────────────────────────────────────────────

def test_tomar_dano_reduz_vida():
    """Deve reduzir corretamente as vidas ao tomar dano."""
    assert tomar_dano(3, 1) == 2


def test_tomar_dano_zera_vida():
    """Deve retornar zero quando o dano é igual às vidas restantes."""
    assert tomar_dano(1, 1) == 0


# ──────────────────────────────────────────────
# jogador_perdeu
# ──────────────────────────────────────────────

def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_perdeu_com_vidas_negativas():
    """Deve indicar derrota mesmo com vidas negativas."""
    assert jogador_perdeu(-1) is True


def test_jogador_nao_perdeu_com_vidas():
    """Não deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_jogador_nao_perdeu_com_uma_vida():
    """Não deve indicar derrota com exatamente uma vida restante."""
    assert jogador_perdeu(1) is False


# ──────────────────────────────────────────────
# limitar_valor
# ──────────────────────────────────────────────

def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite mínimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite máximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele já estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_limitar_valor_no_limite_minimo():
    """Deve retornar o valor quando ele for exatamente o mínimo."""
    assert limitar_valor(0, 0, 100) == 0


def test_limitar_valor_no_limite_maximo():
    """Deve retornar o valor quando ele for exatamente o máximo."""
    assert limitar_valor(100, 0, 100) == 100


# ──────────────────────────────────────────────
# calcular_nivel
# ──────────────────────────────────────────────

def test_calcular_nivel_inicial():
    """Deve retornar nível 1 no início do jogo (frame 0)."""
    assert calcular_nivel(0) == 1


def test_calcular_nivel_antes_do_primeiro_aumento():
    """Deve permanecer no nível 1 antes de completar 1800 frames."""
    assert calcular_nivel(1799) == 1


def test_calcular_nivel_no_primeiro_aumento():
    """Deve avançar para o nível 2 ao completar 1800 frames."""
    assert calcular_nivel(1800) == 2


def test_calcular_nivel_terceiro_nivel():
    """Deve retornar nível 3 ao completar 3600 frames."""
    assert calcular_nivel(3600) == 3


# ──────────────────────────────────────────────
# calcular_taxa_spawn
# ──────────────────────────────────────────────

def test_calcular_taxa_spawn_nivel_1():
    """No nível 1, a taxa de spawn deve ser a taxa base (30)."""
    assert calcular_taxa_spawn(1) == 30


def test_calcular_taxa_spawn_nivel_2():
    """No nível 2, a taxa de spawn deve ser reduzida em 5 (25)."""
    assert calcular_taxa_spawn(2) == 25


def test_calcular_taxa_spawn_nao_abaixo_do_minimo():
    """A taxa de spawn nunca deve ser menor que o mínimo (10)."""
    assert calcular_taxa_spawn(100) == 10
