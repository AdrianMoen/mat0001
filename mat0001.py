# Author: Adrian Løberg Moen
# Github: AdrianMoen
# Email: Adrian.Moen01@gmail.com
import sys
import pygame
from pygame.locals import *

pygame.init()

canvas = pygame.Surface.pygame.Surface.Surface(1280, 720)

class Triangle():

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        
        self.x2 = x2
        self.y2 = y2
        
        self.x3 = x3
        self.y3 = y3

    def draw_triangle(self):
        pass

    def update_triangle(self):
        pass

    # finner bredden på trekanten
    def get_width(x1, x2, x3):

        if x1 < x2:
            if x1 < x3:
                if x2 > x3:
                    width = x2 - x1
                else:
                    width = x3 - x1
            else:
                width = x2 - x3
        else:
            if x2 < x3:
                if x1 > x3:
                    width = x1 - x2
                else:
                    width = x3 - x2
            else:
                width = x1 - x3

        return width

    # finner høyden på trekanten
    def get_height(y1, y2, y3):

        if y1 < y2:
            if y1 < y3:
                if y2 > y3:
                    height = y2 - y1
                else:
                    height = y3 - y1
            else:
                height = y2 - y3
        else:
            if y2 < y3:
                if y1 > y3:
                    height = y1 - y2
                else:
                    height = y3 - y2
            else:
                height = y1 - y3

        return height

# gjør sierpinksi delen om til en klasse, mest for at det skal se pent ut
class SierpinskiTriangle():
    
    def __init__(self, triangle_list):
        self.triangle_list = triangle_list

    # rekursiv funksjon som produserer en liste med alle trekantene
    def calculate_triangle(width, height, triangle_list, n):
        
        new_triangle_list = []

        # lager trekanten som forflyttes til høyre
        for triangle in triangle_list:
            x1New = triangle.x1 + width
            x2New = triangle.x2 + width
            x3New = triangle.x3 + width

            newTriangle = Triangle(x1New, triangle.y1, x2New, triangle.y2, x3New, triangle.y3)
            new_triangle_list.append(newTriangle)
            new_triangle_list.append(triangle)

        # lager trekanten som forflyttes opp of til høyre i midten
        for triangle in triangle_list:
            x1New = triangle.x1 + width/2
            x2New = triangle.x2 + width/2
            x3New = triangle.x3 + width/2

            y1New = triangle.y1 + height
            y2New = triangle.y2 + height
            y3New = triangle.y3 + height

            newTriangle = Triangle(x1New, y1New, x2New, y2New, x3New, y3New)
            new_triangle_list.append(newTriangle)
    
        # fjerner triangle_list for hver gang, siden en ny sendes videre
        del triangle_list

        n = n - 1

        if n <= 0:
            return triangle_list

        SierpinskiTriangle.calculate_triangle(width, height, new_triangle_list, n)



def main():
    
    running = True

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

    # henter inn argumentet
    n = sys.argv[0]

    #lager den første trekanten og legger den inn i den første listen
    triangle = Triangle()
    triangle_list.append(triangle)

    complete_triangle_liste = SierpinskiTriangle.calculate_triangle(width, height, triangle_list, n)

    while running:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                runnign = False
                pygame.display.quit()
                pygame.quit()

if __name__ == '__main__':
    main()