import pygame 
from pygame.locals import *

pygame.init()
pygame.front.init()

canvas = pygame.Surface.pygame.Surface.Surface(1280, 720)

def loop():
    
    runnign = True

    while runnign:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                runnign = False
                pygame.display.quit()
                pygame.quit()

        



if __name__ == '__main__':
    loop()