# Author: Adrian Løberg Moen
# Github: AdrianMoen
# Email: Adrian.Moen01@gmail.com
import sys
import pygame
from pygame import color
from pygame.locals import *

pygame.init()

window_width = 1280
window_height = 720

screencolor = (0, 0, 0)

canvas = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sierpinski trekant")

class Triangle():

    def __init__(self, x1, y1, x2, y2, x3, y3, surface):
        self.x1 = x1
        self.y1 = y1
        
        self.x2 = x2
        self.y2 = y2
        
        self.x3 = x3
        self.y3 = y3
        
        self.surface = surface

    def draw_triangle(self, color):

        pygame.draw.line(self.surface, color, (self.x1, self.y1), (self.x2, self.y2), width=1)
        pygame.draw.line(self.surface, color, (self.x2, self.y2), (self.x3, self.y3), width=1)
        pygame.draw.line(self.surface, color, (self.x3, self.y3), (self.x1, self.y1), width=1)

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
    
    def __init__(self, triangle_list, n):
        self.triangle_list = triangle_list
        self.n = n

    # rekursiv funksjon som produserer en liste med alle trekantene
    def calculate_triangles(width, height, triangle_list, n):
        
        new_triangle_list = []

        # sjekker om vi har nådd n-te iterasjon, dersom n == 1
        # returnerer vi den originale trekant listen
        if n <= 1:
            return triangle_list

        # lager trekanten som forflyttes til høyre
        for triangle in triangle_list:
            x1New = triangle.x1 + width
            x2New = triangle.x2 + width
            x3New = triangle.x3 + width

            newTriangle = Triangle(x1New, triangle.y1, x2New, triangle.y2, x3New, triangle.y3, canvas)
            new_triangle_list.append(newTriangle)
            new_triangle_list.append(triangle)

        # lager trekanten som forflyttes opp of til høyre i midten
        for triangle in triangle_list:
            x1New = triangle.x1 + width/2
            x2New = triangle.x2 + width/2
            x3New = triangle.x3 + width/2
            
            y1New = triangle.y1 - height
            y2New = triangle.y2 - height
            y3New = triangle.y3 - height

            newTriangle = Triangle(x1New, y1New, x2New, y2New, x3New, y3New, canvas)
            new_triangle_list.append(newTriangle)
    
        # fjerner triangle_list for hver gang, siden en ny sendes videre
        del triangle_list

        width  *= 2
        height *= 2

        n = n - 1

        return_list = SierpinskiTriangle.calculate_triangles(width, height, new_triangle_list, n)
        return return_list

    def orient_triangles(triangle_list, width, height, n):
        
        # Vilkårlig verdi som burde være vere mer en den minste x verdien
        minX = 10000

        # finner, og oppdaterer minX med den minste x verdien
        for triangle in triangle_list:
            x1 = triangle.x1
            x2 = triangle.x2
            x3 = triangle.x3

            if x1 < x2:
                if x1 < x3:
                    if x1 < minX:
                        minX = x1
                        continue
                    else:
                        continue
                else:
                    if x3 < minX:
                        minX = x3
                        continue
                    else:
                        continue
            else:
                if x2 < x3:
                    if x2 < minX:
                        minX = x2
                        continue
                    else:
                        continue
                else:
                    if x3 < minX:
                        minX = x3
                        continue
                    else:
                        continue

        # Siden trekanten vokser i positiv x, og negativ y, må vi finne maxY
        maxY = -10000

        for triangle in triangle_list:
            y1 = triangle.y1
            y2 = triangle.y2
            y3 = triangle.y3

            if y1 > y2:
                if y1 > y3:
                    if y1 > maxY:
                        maxY = y1
                        continue
                    else:
                        continue
                else:
                    if y3 > maxY:
                        maxY = y3
                        continue
                    else:
                        continue
            else:
                if y2 > y3:
                    if y2 > maxY:
                        maxY = y2
                        continue
                    else:
                        continue
                else:
                    if y3 > maxY:
                        maxY = y3
                        continue
                    else:
                        continue

        print("minX: ",minX)
        print("maxY: ",maxY)

        for triangle in triangle_list:
            triangle.x1 = (triangle.x1/2**n)*12
            triangle.x2 = (triangle.x2/2**n)*12
            triangle.x3 = (triangle.x3/2**n)*12

            triangle.y1 = (triangle.y1/2**n)*12
            triangle.y2 = (triangle.y2/2**n)*12
            triangle.y3 = (triangle.y3/2**n)*12

            triangle.x1 += minX
            triangle.x2 += minX
            triangle.x3 += minX

            triangle.y1 += maxY
            triangle.y2 += maxY
            triangle.y3 += maxY



def main():
    
    running = True

    # posisjon til første trekant
    x1 = 100
    y1 = 100

    x2 = 200
    y2 = 100

    x3 = 150
    y3 = 0

    # fargen til trekantene representert av en tuple med rgb verdier
    # og en alpha verdi, alle trekantene skal ha samme farge.
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)
    cyan = (0, 255, 255, 255)
    white = (255, 255, 255, 255)

    color = cyan

    # finner bredde og høyde, som er statisk gjennom programmet
    width = Triangle.get_width(x1, x2, x3)
    height = Triangle.get_height(y1, y2, y3)

    # henter inn argumentet og gjøre det om til int,
    # siden den tolkes som en string, eller 'str'
    n = int(sys.argv[1])

    # lager den første trekanten og legger den inn i den første listen
    triangle_list = []
    triangle = Triangle(x1, y1, x2, y2, x3, y3, canvas)
    triangle_list.append(triangle)


    # lager sierpinski trekanten av n-te grad
    p = 1
    complete_triangle_list = SierpinskiTriangle.calculate_triangles(width, height, triangle_list, n)

    # initialiserer sierpinski trekanten
    sierpinski = SierpinskiTriangle(complete_triangle_list, n)

    # forflytter trekantene slik at de er synlige, samt skalerer dem
    SierpinskiTriangle.orient_triangles(complete_triangle_list, width, height, n)

    # hoved loop for å displaye trekanten
    while running:
        
        canvas.fill(screencolor)

        # tegner alle trekantene. Trenger strengt tatt ikke
        # være inne i hoved loopen, da de ikke flytter på seg
        for triangle in complete_triangle_list:
            triangle.draw_triangle(color)
        # print(len(complete_triangle_list))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnign = False
                pygame.display.quit()
                pygame.quit()

if __name__ == '__main__':
    main()