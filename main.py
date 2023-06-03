import pygame

def initialize_game():
    """Inicializa o Pygame e configura a janela do jogo."""
    pygame.init()
    gameWindow = pygame.display.set_mode([1200, 600])
    pygame.display.set_caption('Reisen Fortsetter')
    return gameWindow

def draw(gameWindow):
    """Preenche a janela do jogo com uma cor de fundo."""
    gameWindow.fill([119, 136, 153])

def handle_events():
    """Lida com os eventos do Pygame, como fechar a janela do jogo."""
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()

def handle_movement(comands, x, y, speed):
    """Lida com o movimento do objeto com base nas teclas pressionadas."""
    if comands[pygame.K_UP]:
        y -= speed
    elif comands[pygame.K_DOWN]:
        y += speed
    elif comands[pygame.K_LEFT]:
        x -= speed
    elif comands[pygame.K_RIGHT]:
        x += speed
    return x, y

def draw_circle(gameWindow, x, y):
    """Desenha um círculo na janela do jogo nas coordenadas (x, y)."""
    pygame.draw.circle(gameWindow, (0,255,0), (x, y), 50)

def update_display():
    """Atualiza a exibição da janela do jogo."""
    pygame.display.update()

def game_loop(gameWindow):
    """Loop principal do jogo."""
    gameLoop = True
    x, y, speed = 600, 300, 0.5
    
    pygame.time.delay(50)

    while gameLoop:
        handle_events()

        comands = pygame.key.get_pressed()
        x, y = handle_movement(comands, x, y, speed)

        draw(gameWindow)
        draw_circle(gameWindow, x, y)
        update_display()

if __name__ == '__main__':
    gameWindow = initialize_game()
    game_loop(gameWindow)
