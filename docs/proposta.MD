# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Aventura Galáctica: Defesa Estelar

## 2. Integrantes do grupo

- Nome 1: Rafael Melo Mansur Cardoso

## 3. Tipo de jogo

> Nave desviando de meteoros e coletando recursos.

## 4. Descrição geral do jogo

> O jogo consiste de uma nave espacial no centro inferior da tela que pode se mover para os lados. Meteoros caem do topo da tela em velocidades variadas e o jogador tem que desviar. Ocasionalmente, cristais de energia (itens de coleta) caem e devem ser coletados para aumentar a pontuação. Conforme o tempo passa, a frequência de meteoros aumenta.

## 5. Objetivo do jogador

> Sobreviver pelo maior tempo possível e acumular a maior pontuação através da coleta de cristais e tempo de sobrevivência.

## 6. Regras principais

- O jogador começa com 3 vidas.
- Cada cristal coletado vale 50 pontos.
- Colidir com um meteoro remove 1 vida.
- A cada 30 segundos, a velocidade de queda dos meteoros aumenta levemente.
- A partida termina quando as vidas chegam a zero.

## 7. Condição de vitória

> Por ser um jogo de sobrevivência, não tem uma "vitória" definitiva, mas o jogador vence o seu próprio recorde que será salvo.

## 8. Condição de derrota ou encerramento

> Perder todas as 3 vidas ao colidir com meteoros.

## 9. Elementos previstos no jogo

- Jogador ou elemento principal

> Uma nave espacial controlada pelas setas esquerda e direita do teclado.

- Obstáculos, inimigos ou desafios

> Meteoros de diferentes tamanhos que caem do topo da tela em posições aleatórias.

- Itens, alvos ou objetos de interação

> Cristais de energia brilhantes que aparecem raramente e dão bônus de pontuação.

- Pontuação, vidas, tempo ou progresso

> Display no topo da tela mostrando Vidas (ícones de coração ou texto), Pontuação Atual e Tempo de Jogo.

## 10. Controles previstos

- Seta para esquerda: mover nave para a esquerda
- Seta para direita: mover nave para a direita
- ESC: sair do jogo / pausar
- R: reiniciar o jogo na tela de Game Over

## 11. Organização inicial do código

- `main.py`: Ponto de entrada que inicializa o Pygame e chama o loop principal.
- `src/engine.py`: Gerencia o loop do jogo, estados (menu, jogando, game over) e eventos.
- `src/entities.py`: Define as classes para Nave, Meteoro e Cristal.
- `src/settings.py`: Constantes como cores, tamanho da tela, e velocidades iniciais.
- `src/utils.py`: Funções para carregar assets e manipular arquivos de recorde (JSON/TXT).

## 12. Recursos externos previstos

> Imagens de naves e meteoros de bancos gratuitos (ex: Kenney.nl ou OpenGameArt). Sons de explosão e coleta simples.

## 13. Principais dificuldades esperadas

- Detecção de colisão precisa entre a nave e os meteoros.
- Gerenciamento eficiente da geração aleatória de objetos para não sobrecarregar a tela.
- Implementação correta da persistência do recorde em arquivo.

## 14. Escopo mínimo para a entrega final

> Uma nave funcional que se move, meteoros caindo que causam perda de vida, sistema de pontuação por tempo, tela de Game Over e salvamento de recorde.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Sistema de "tiro" para destruir meteoros pequenos.
- Diferentes tipos de naves para escolher.
- Trilha sonora de fundo e efeitos sonoros variados.
- Power-ups temporários (ex: escudo ou velocidade).
