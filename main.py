import pygame

pygame.init()
gameWindow = pygame.display.set_mode([1200, 600])
pygame.display.set_caption('Reisen Fortsetter')

def draw():
    gameWindow.fill([119, 136, 153])

def loop():
    gameLoop = True
    x, y, speed = 600, 300, 0.5
    
    pygame.time.delay(50)

    while gameLoop:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
            
        comands = pygame.key.get_pressed()

        if comands[pygame.K_UP]:
            y -= speed
        elif comands[pygame.K_DOWN]:
            y += speed
        elif comands[pygame.K_LEFT]:
            x -= speed
        elif comands[pygame.K_RIGHT]:
            x += speed

        draw()

        pygame.draw.circle(gameWindow, (0,255,0), (x, y), 50)
        pygame.display.update()

if __name__ == '__main__':
    loop()
