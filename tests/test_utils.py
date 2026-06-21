"""
Testes das funções de persistência de dados (src/utils.py):
recorde (highscore) e ranking.
"""
import pytest
import os
from src.utils import (
    carregar_recorde,
    salvar_recorde,
    carregar_ranking,
    salvar_ranking,
)
from src.settings import ARQUIVO_RECORDE, ARQUIVO_RANKING


# ──────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────

@pytest.fixture(autouse=True)
def limpar_arquivos_de_dados():
    """Remove os arquivos de dados antes e depois de cada teste."""
    for caminho in (ARQUIVO_RECORDE, ARQUIVO_RANKING):
        if os.path.exists(caminho):
            os.remove(caminho)
    yield
    for caminho in (ARQUIVO_RECORDE, ARQUIVO_RANKING):
        if os.path.exists(caminho):
            os.remove(caminho)


# ──────────────────────────────────────────────
# Testes de Recorde
# ──────────────────────────────────────────────

def test_carregar_recorde_sem_arquivo():
    """Deve retornar 0 quando o arquivo de recorde não existe."""
    assert carregar_recorde() == 0


def test_salvar_recorde_novo():
    """Deve salvar e recuperar corretamente um novo recorde."""
    salvar_recorde(100)
    assert carregar_recorde() == 100


def test_salvar_recorde_menor_nao_sobrescreve():
    """Um score menor não deve sobrescrever o recorde existente."""
    salvar_recorde(100)
    salvar_recorde(50)
    assert carregar_recorde() == 100


def test_salvar_recorde_igual_nao_sobrescreve():
    """Um score igual ao recorde não deve sobrescrever o arquivo."""
    salvar_recorde(100)
    resultado = salvar_recorde(100)
    assert resultado is False
    assert carregar_recorde() == 100


def test_salvar_recorde_maior_atualiza():
    """Um score maior deve atualizar o recorde e retornar True."""
    salvar_recorde(100)
    resultado = salvar_recorde(200)
    assert resultado is True
    assert carregar_recorde() == 200


def test_carregar_recorde_conteudo_invalido():
    """Deve retornar 0 quando o arquivo contém conteúdo não numérico."""
    os.makedirs(os.path.dirname(ARQUIVO_RECORDE), exist_ok=True)
    with open(ARQUIVO_RECORDE, "w") as arquivo:
        arquivo.write("abc")
    assert carregar_recorde() == 0


# ──────────────────────────────────────────────
# Testes de Ranking
# ──────────────────────────────────────────────

def test_carregar_ranking_sem_arquivo():
    """Deve retornar lista vazia quando o arquivo de ranking não existe."""
    assert carregar_ranking() == []


def test_salvar_ranking_uma_pontuacao():
    """Deve salvar e recuperar uma pontuação no ranking."""
    salvar_ranking(150)
    assert carregar_ranking() == [150]


def test_salvar_ranking_ordena_decrescente():
    """O ranking deve ser retornado em ordem decrescente."""
    salvar_ranking(100)
    salvar_ranking(300)
    salvar_ranking(200)
    ranking = carregar_ranking()
    assert ranking == [300, 200, 100]


def test_salvar_ranking_limite_cinco_entradas():
    """O ranking deve manter no máximo 5 entradas (as maiores)."""
    for pontuacao in [10, 20, 30, 40, 50, 60]:
        salvar_ranking(pontuacao)
    ranking = carregar_ranking()
    assert len(ranking) == 5
    assert ranking[0] == 60
    assert 10 not in ranking
