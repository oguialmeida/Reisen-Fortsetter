import pygame
from utils.events import handle_events
from utils.drawing import draw, draw_circle, update_display
from utils.movement import handle_movement, clamp

def initialize_game():
    """Inicializa o Pygame e configura a janela do jogo."""
    pygame.init()
    gameWindow = pygame.display.set_mode([1200, 600])
    pygame.display.set_caption('Reisen Fortsetter')
    return gameWindow

def game_loop(gameWindow):
    """Loop principal do jogo."""
    gameLoop = True
    x, y, speed = 600, 300, 0.5
    window_width, window_height = gameWindow.get_size()
    circle_radius = 50
    
    pygame.time.delay(50)

    while gameLoop:
        handle_events()

        comands = pygame.key.get_pressed()
        x, y = handle_movement(comands, x, y, speed)

        # Limita as coordenadas x e y dentro dos limites da janela
        x = clamp(x, circle_radius, window_width - circle_radius)
        y = clamp(y, circle_radius, window_height - circle_radius)

        draw(gameWindow)
        draw_circle(gameWindow, x, y)
        update_display()

if __name__ == '__main__':
    gameWindow = initialize_game()
    game_loop(gameWindow)
