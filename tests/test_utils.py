import pytest
import os
from src.utils import load_highscore, save_highscore
from src.settings import DATA_FILE

# Garante que o arquivo de dados de teste é limpo antes de cada teste
@pytest.fixture(autouse=True)
def cleanup_data_file():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    yield
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_load_highscore_initial():
    """Testa se o recorde é carregado como 0 quando o arquivo não existe."""
    assert load_highscore() == 0

def test_save_highscore_new_record():
    """Testa se um novo recorde é salvo corretamente."""
    save_highscore(100)
    assert load_highscore() == 100

def test_save_highscore_lower_score():
    """Testa se um score menor não sobrescreve o recorde."""
    save_highscore(100)
    save_highscore(50)
    assert load_highscore() == 100

def test_save_highscore_equal_score():
    """Testa se um score igual não sobrescreve o recorde."""
    save_highscore(100)
    save_highscore(100)
    assert load_highscore() == 100

def test_load_highscore_invalid_content():
    """Testa o carregamento de recorde com conteúdo inválido no arquivo."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        f.write("abc")
    assert load_highscore() == 0
