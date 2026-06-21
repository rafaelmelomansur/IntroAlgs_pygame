"""
Funções auxiliares de lógica pura do jogo.
Estas funções não dependem do Pygame e podem ser testadas de forma isolada.
"""


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual e retorna o novo total."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido e retorna o novo total."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Retorna True se o jogador ficou sem vidas, False caso contrário."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def calcular_nivel(contador_frames, frames_por_nivel=1800):
    """Calcula o nível de dificuldade com base no número de frames decorridos.
    O nível aumenta a cada 'frames_por_nivel' frames (padrão: 30 segundos a 60 FPS).
    """
    return 1 + contador_frames // frames_por_nivel


def calcular_taxa_spawn(nivel, taxa_base=30, reducao_por_nivel=5, taxa_minima=10):
    """Calcula a taxa de geração de meteoros conforme o nível de dificuldade.
    Quanto maior o nível, menor o intervalo entre spawns (mais meteoros).
    """
    return max(taxa_minima, taxa_base - (nivel - 1) * reducao_por_nivel)
