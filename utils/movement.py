import pygame

def handle_movement(comands, x, y, speed):
    # Lida com o movimento do objeto com base nas teclas pressionadas.
    if comands[pygame.K_UP]:
        y -= speed
    elif comands[pygame.K_DOWN]:
        y += speed
    elif comands[pygame.K_LEFT]:
        x -= speed
    elif comands[pygame.K_RIGHT]:
        x += speed
    return x, y

def clamp(value, min_value, max_value):
    # Limita o valor dentro de um intervalo.
    return max(min(value, max_value), min_value)
