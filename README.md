# Aventura Galáctica: Defesa Estelar

Projeto final da disciplina de Introdução a Algoritmos, desenvolvido com Python e Pygame.

Este repositório contém a versão final do jogo "Aventura Galáctica: Defesa Estelar", onde o jogador controla uma nave espacial para desviar de meteoros e coletar cristais de energia.

## Integrantes do grupo

- Rafael Melo Mansur Cardoso

## Estrutura do projeto

- `main.py`: Ponto de entrada que inicializa o Pygame e chama o loop principal.
- `src/engine.py`: Gerencia o loop do jogo, estados (telas de início, jogando, game over), eventos, aumento de dificuldade e renderização.
- `src/entities.py`: Define as classes de sprites para a Nave (Jogador), Meteoro e Cristal.
- `src/settings.py`: Constantes e configurações do jogo, como cores, tamanho da tela, pontuações e velocidades iniciais.
- `src/utils.py`: Funções para manipular persistência de dados (recorde e ranking em arquivo de texto).
- `src/funcoes.py`: Funções puras de lógica do jogo (cálculo de pontos, dano, colisões, nível de dificuldade).
- `assets/`: Imagens e sprites utilizados no jogo (Kenney Space Shooter).
- `data/`: Arquivos persistentes (`highscore.txt` e `ranking.txt`).
- `tests/`: Testes automatizados implementados com `pytest` para as funções de lógica e persistência.
- `docs/`: Documentação do projeto, incluindo a proposta inicial (`proposta.md`).

## Descrição do jogo

O jogo apresenta uma nave espacial no centro inferior da tela que pode se mover horizontalmente. Meteoros caem do topo da tela em velocidades variadas e o jogador deve desviá-los. Ocasionalmente, cristais de energia caem e devem ser coletados para aumentar a pontuação. Conforme o tempo passa, o nível de dificuldade aumenta, fazendo com que a frequência e a velocidade dos meteoros também aumentem.

## Regras e Objetivos

- **Objetivo**: Sobreviver pelo maior tempo possível e acumular a maior pontuação através da coleta de cristais e tempo de sobrevivência.
- **Vidas**: O jogador começa com 3 vidas. Colidir com um meteoro remove 1 vida e destrói o meteoro. A partida termina quando as vidas chegam a zero.
- **Pontuação**: Cada cristal coletado vale 50 pontos. Além disso, o jogador ganha 1 ponto a cada segundo sobrevivido.
- **Dificuldade**: A cada 30 segundos de sobrevivência, o nível do jogo aumenta, o que aumenta a velocidade máxima dos meteoros e a quantidade gerada.
- **Ranking e Recorde**: O jogo mantém salvo o recorde absoluto de pontuação, além de um Top 5 com as melhores pontuações registradas localmente.

## Controles

- **Seta para esquerda (←)**: mover a nave para a esquerda
- **Seta para direita (→)**: mover a nave para a direita
- **ESC**: sair do jogo ou voltar nas telas
- **R**: reiniciar o jogo rapidamente na tela de Game Over

## Como executar o projeto

Certifique-se de ter o Python instalado na sua máquina (versão 3.8 ou superior).

### 1. Instalar as dependências

Instale as bibliotecas necessárias (Pygame e Pytest) utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Executar o jogo

No diretório raiz do projeto, execute o arquivo principal:

```bash
python main.py
```

## Como executar os testes

Os testes automatizados garantem o funcionamento correto da lógica de pontuação, dano, níveis e salvamento de arquivos. Para rodá-los, utilize o pytest:

```bash
python -m pytest tests/ -v
```

## Recursos externos utilizados (Assets)

Os recursos visuais deste jogo pertencem ao pacote **Space Shooter Redux**, criado por Kenney Vleugels.
- **Autor**: Kenney Vleugels (www.kenney.nl)
- **Licença**: Domínio Público (CC0 1.0 Universal)
- **Fonte**: [Kenney Assets - Space Shooter Redux](https://kenney.nl/assets/space-shooter-redux)
