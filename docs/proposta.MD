# Proposta do Jogo: Aventura Galáctica: Defesa Estelar

## 1. Integrantes do grupo

- Rafael Melo Mansur Cardoso

## 2. Tipo de jogo

> Jogo de sobrevivência 2D: Nave desviando de meteoros e coletando recursos.

## 3. Descrição geral do jogo

> O jogo consiste em uma nave espacial no centro inferior da tela que pode se mover horizontalmente. Meteoros caem do topo da tela em velocidades variadas e o jogador tem que desviar. Ocasionalmente, cristais de energia caem e devem ser coletados para aumentar a pontuação. Conforme o tempo passa, o nível do jogo aumenta, o que eleva a frequência e a velocidade dos meteoros.

## 4. Objetivo do jogador

> Sobreviver pelo maior tempo possível e acumular a maior pontuação através da coleta de cristais e do tempo de sobrevivência, tentando bater o próprio recorde e alcançar o Top 5 do ranking local.

## 5. Regras principais

- O jogador começa com 3 vidas.
- Cada cristal coletado vale 50 pontos.
- A cada 1 segundo sobrevivido, o jogador ganha 1 ponto.
- Colidir com um meteoro remove 1 vida e destrói o meteoro.
- A cada 30 segundos, o nível de dificuldade do jogo aumenta, elevando a velocidade máxima e a quantidade de meteoros.
- A partida termina quando as vidas chegam a zero.

## 6. Condição de vitória

> Por ser um jogo infinito de sobrevivência, não há uma "vitória" definitiva, mas o jogador vence ao superar seu próprio recorde e entrar no Top 5 de pontuações salvas.

## 7. Condição de derrota ou encerramento

> Perder todas as 3 vidas ao colidir com os meteoros.

## 8. Elementos implementados no jogo

- **Jogador (Nave):**
> Uma nave espacial controlada pelas setas esquerda e direita do teclado.

- **Obstáculos (Meteoros):**
> Meteoros de diferentes tamanhos que caem do topo da tela em posições aleatórias. A velocidade e quantidade dependem do nível de dificuldade atual.

- **Itens (Cristais):**
> Cristais de energia brilhantes que aparecem mais raramente e dão bônus significativos de pontuação.

- **HUD (Interface):**
> Display no topo da tela mostrando a Pontuação Atual, Vidas restantes, Nível atual e o Recorde Absoluto.

## 9. Controles

- **Seta para esquerda (←)**: mover a nave para a esquerda
- **Seta para direita (→)**: mover a nave para a direita
- **ESC**: sair do jogo ou fechar a tela de game over
- **R**: reiniciar o jogo rapidamente a partir da tela de Game Over

## 10. Organização do código

- `main.py`: Ponto de entrada que inicializa o Pygame e chama o loop principal.
- `src/engine.py`: Controla o loop principal, as telas (Início, Jogo, Game Over), o aumento progressivo de dificuldade e os eventos.
- `src/entities.py`: Define as classes de Sprites para Nave, Meteoro e Cristal.
- `src/settings.py`: Guarda as configurações globais, cores, pontuações e velocidades.
- `src/utils.py`: Funções para manipular a persistência em arquivos de texto (recorde e ranking) e renderização de texto.
- `src/funcoes.py`: Funções puras de lógica do jogo.

## 11. Recursos externos utilizados

> As imagens da nave, meteoros, cristais e fundo pertencem ao pacote **Space Shooter Redux** do banco gratuito **Kenney.nl** (Licença CC0).

## 12. Principais desafios encontrados

- Implementar o aumento progressivo de dificuldade equilibrando a velocidade e a taxa de spawn dos meteoros sem tornar o jogo impossível muito rápido.
- Estruturar o código para que o loop principal (`engine.py`) ficasse limpo e a lógica pura fosse separada (`funcoes.py`) para facilitar os testes automatizados com `pytest`.
- Gerenciar corretamente a gravação de dados em arquivos de texto simples, garantindo que o arquivo não corrompesse e que o ranking de Top 5 ficasse ordenado.

## 13. Escopo final entregue

> Uma nave funcional que se move horizontalmente; meteoros caindo com colisão por máscara de pixel (hitbox preciso); perda de vida ao colidir; sistema de pontuação híbrido (tempo e coleta de cristais); dificuldade que escala por tempo (níveis); telas de Início e Game Over; salvamento de Recorde Absoluto e Ranking (Top 5) em arquivos `.txt`.
