import pygame

def draw(gameWindow):
    """Preenche a janela do jogo com uma cor de fundo."""
    gameWindow.fill([119, 136, 153])

def draw_circle(gameWindow, x, y):
    """Desenha um círculo na janela do jogo nas coordenadas (x, y)."""
    pygame.draw.circle(gameWindow, (0,255,0), (x, y), 50)

def update_display():
    """Atualiza a exibição da janela do jogo."""
    pygame.display.update()
