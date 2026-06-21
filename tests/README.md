# Testes

Esta pasta contém testes automatizados do projeto utilizando `pytest`.

## Arquivos

- `test_logica.py`: valida funções puras de lógica (pontos, dano, níveis) em `src/funcoes.py`.
- `test_utils.py`: valida a persistência em arquivos (recorde e ranking) de `src/utils.py`.

## Como executar

```bash
python -m pytest tests/ -v
```
