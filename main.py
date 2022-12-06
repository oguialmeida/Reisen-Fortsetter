import pygame

# Inicia a janela
pygame.init()
# Define o tamanho dele
gameWindow = pygame.display.set_mode([1200, 600])
# Define um nome para a janela
pygame.display.set_caption('Reisen Fortsetter')

# Define uma cor de fundo
def draw():
    gameWindow.fill([119, 136, 153])


def loop():
    gameLoop = True # Enquanto a janela aberta for vedadeira
    while gameLoop:
        for event in pygame.event.get(): # Vai cair em uma condição caso algúm evento seja disparado
            if event.type == pygame.QUIT: # Saber qual evento que foi feito e fazer uma ação relacionada a isso
                pygame.quit()
                break
        draw()
        pygame.display.update()


if __name__ == '__main__':
    loop()
