import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.front.init()

canvas = pygame.Surface.pygame.Surface.Surface(1280, 720)

class Triangle():

    def __init__(self, x1, y1, x2, y2, x3, y3):
        pass

    def draw_triangle(self):
        pass

    def update_triangle(self):
        pass

    def get_width(x1, x2, x3):
        if x1 > x2:
            pass
        else:
            if x2 > x3:
                pass
            else:
                pass

    def get_height(y1, y2, y3):
        pass



def calculate_triangle(width, height, triangkle_list):
    pass



def main():
    
    runnign = True

    # posisjon til første trekant
    x1 = 100
    y1 = 100

    x2 = 200
    y2 = 100

    x3 = 50
    y3 = 0

    # finner bredde og høyde, som er statisk gjennom programmet
    width = Triangle.get_width(x1, x2, x3)
    height = Triangle.get_height(y1, y2, y3)

    triangle_list = []

    n = sys.argv[0]

    i = 0

    while runnign:

        triangle = Triangle()
        list.append(triangle)

        while i > n:
            calculate_triangle()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                runnign = False
                pygame.display.quit()
                pygame.quit()

if __name__ == '__main__':
    main()