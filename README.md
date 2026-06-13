# Aventura Galáctica: Defesa Estelar

Projeto final da disciplina de Introdução a Algoritmos, desenvolvido com Python e Pygame.

Este repositório contém o jogo "Aventura Galáctica: Defesa Estelar", onde o jogador controla uma nave espacial para desviar de meteoros e coletar cristais de energia.

## Integrantes do grupo

- Rafael Melo Mansur Cardoso

## Estrutura do projeto

- `main.py`: Ponto de entrada que inicializa o Pygame e chama o loop principal.
- `src/engine.py`: Gerencia o loop do jogo, estados (menu, jogando, game over) e eventos.
- `src/entities.py`: Define as classes para Nave, Meteoro e Cristal.
- `src/settings.py`: Constantes como cores, tamanho da tela, e velocidades iniciais.
- `src/utils.py`: Funções para carregar assets e manipular arquivos de recorde (JSON/TXT).
- `assets/`: Imagens, fontes e sons (a serem adicionados).
- `data/`: Arquivos persistentes (recorde/ranking).
- `tests/`: Testes unitários com `pytest` (a serem implementados).
- `docs/`: Documentação do projeto, incluindo proposta inicial (`proposta.MD`).

## Descrição do jogo

O jogo apresenta uma nave espacial no centro inferior da tela que pode se mover horizontalmente. Meteoros caem do topo da tela em velocidades variadas e o jogador deve desviá-los. Ocasionalmente, cristais de energia (itens de coleta) caem e devem ser coletados para aumentar a pontuação. Conforme o tempo passa, a frequência de meteoros aumenta.

## Objetivo do jogador

Sobreviver pelo maior tempo possível e acumular a maior pontuação através da coleta de cristais e tempo de sobrevivência.

## Regras do jogo

- O jogador começa com 3 vidas.
- Cada cristal coletado vale 50 pontos.
- Colidir com um meteoro remove 1 vida e destrói o meteoro.
- A cada 30 segundos, a velocidade de queda dos meteoros aumenta levemente.
- A partida termina quando as vidas chegam a zero.

## Controles

- Seta para esquerda: mover nave para a esquerda
- Seta para direita: mover nave para a direita
- ESC: sair do jogo / pausar
- R: reiniciar o jogo na tela de Game Over

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template.git
cd IntroAlgs_pygame_template
pip install -r requirements.txt
python main.py
```

### 2. Executar o jogo

Após clonar o repositório e instalar as dependências, execute o arquivo `main.py`:

```bash
python main.py
```

## Como executar os testes

```bash
python -m pytest
```