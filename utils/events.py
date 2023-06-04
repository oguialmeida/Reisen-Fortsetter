import pygame

def handle_events():
    # Lida com os eventos do Pygame, como fechar a janela do jogo.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
