# Author: Adrian Løberg Moen
# Github: AdrianMoen
# Email: Adrian.Moen01@gmail.com
import sys
import pygame
import pygame.gfxdraw
from pygame import color
from pygame.locals import *

pygame.init()

# Vindus dimensjoner
window_width = 1280
window_height = 720

# Skjerm bakgrunnsfarge
screencolor = (0, 0, 0)

# Setter opp pygame sin display og ett canvas
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

    # Tegner selve trekanten ved bruk av gfxdraw, en kan også ender det til filled_trigon()
    def draw_triangle(self, color):
        
        pygame.gfxdraw.trigon(self.surface, int(self.x1), int(self.y1), int(self.x2), int(self.y2), int(self.x3), int(self.y3), color)



    # Finner bredden på trekanten, teknisk sett kan dette gjøres slik det er
    # gjort lengre ned, der det er forutsatt at x1 > x2 > x3. men dette funker
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

    # Finner høyden på trekanten, teknisk sett kan dette gjøres slik det er gjort
    # lengre ned, der det er forutsatt at y2 er størst, og y1 = y3 men dette funker
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

# Gjør sierpinksi delen om til en klasse, mest for at det skal se pent ut
class SierpinskiTriangle():
    
    def __init__(self, triangle_list, n):
        self.triangle_list = triangle_list
        self.n = n

    # Rekursiv funksjon som produserer en liste med alle trekantene
    def calculate_triangles(width, height, triangle_list, n):
        
        # Ny liste for å lagre de nye trekantene som skal videre i rekursjonen
        new_triangle_list = []

        # Sjekker om vi har nådd n-te iterasjon
        if n <= 1:
            return triangle_list

        # Lager trekanten som forflyttes til høyre og legges til i den nye lista
        for triangle in triangle_list:
            x1New = triangle.x1 + width
            x2New = triangle.x2 + width
            x3New = triangle.x3 + width

            newTriangle = Triangle(x1New, triangle.y1, x2New, triangle.y2, x3New, triangle.y3, canvas)
            # Den "originale" trekanten legges til i den nye lista og blir med videre.
            new_triangle_list.append(newTriangle)
            new_triangle_list.append(triangle)

        # Lager trekanten som forflyttes opp of til høyre i midten, og legger til i den nye lista
        for triangle in triangle_list:
            x1New = triangle.x1 + width/2
            x2New = triangle.x2 + width/2
            x3New = triangle.x3 + width/2
            
            y1New = triangle.y1 - height
            y2New = triangle.y2 - height
            y3New = triangle.y3 - height

            newTriangle = Triangle(x1New, y1New, x2New, y2New, x3New, y3New, canvas)
            new_triangle_list.append(newTriangle)
    
        # Fjerner triangle_list for hver gang, siden en ny sendes videre
        del triangle_list

        # Skalerer trekantens bredde slik at de nestkommende 
        # plasseres riktig
        width  *= 2
        height *= 2

        # Reduserer n
        n = n - 1

        # Kaller seg selv rekursivt
        return_list = SierpinskiTriangle.calculate_triangles(width, height, new_triangle_list, n)
        return return_list

    def orient_triangles(triangle_list, n):
    
        # Skalerer trekantene, her er 23 et vilkårlig tall slik at trekanten blir en passe størelse
        # Trekantens bredde øker med 2^n, derav deles den på 2^n 
        for triangle in triangle_list:
            triangle.x1 = ((triangle.x1*23)/2**(n+1))
            triangle.x2 = ((triangle.x2*23)/2**(n+1))
            triangle.x3 = ((triangle.x3*23)/2**(n+1))

            triangle.y1 = ((triangle.y1*23)/2**(n+1))
            triangle.y2 = ((triangle.y2*23)/2**(n+1))
            triangle.y3 = ((triangle.y3*23)/2**(n+1))

        # Vilkårlig verdi som burde være vere mer en den minste x verdien 
        # og større enn den største, bare en liten hack
        minX = 10000
        maxX= -10000

        # Finner, og oppdaterer minX med den minste og største x verdien
        for triangle in triangle_list:
            x1 = triangle.x1
            x2 = triangle.x2
            x3 = triangle.x3

            # Bare x1 kan være minst
            if x1 < minX:
                minX = x1

            # Bare x3 kan være størst
            if x3 > maxX:
                maxX = x3

        # Siden trekanten vokser i positiv x, og negativ y, må vi finne maxY
        maxY = -10000

        for triangle in triangle_list:
            y1 = triangle.y1
            y2 = triangle.y2
            y3 = triangle.y3

            # y1 og y2 er altid minst, siden det er en likesidet trekant. 
            # valget av y1 er helt vilkårlig
            if y1 > maxY:
                maxY = y1

        # Samtlige tall som trengs for å finne moveX og moveY
        # som er forflyttning på x og y aksen
        width = maxX-minX
        startingX = window_width/2 - width/2
        startingY = window_height - 100

        moveX = minX - startingX
        moveY = startingY - maxY

        # Flytter trekanten slik at minX er ved startingX, samme for maxY
        for triangle in triangle_list:

            triangle.x1 -= moveX
            triangle.x2 -= moveX
            triangle.x3 -= moveX
            
            triangle.y1 += moveY
            triangle.y2 += moveY
            triangle.y3 += moveY



def main():
    
    # Mens denne er sann, vill hoved loopen kjøre
    running = True

    # posisjon til den første trekanten
    x1 = 100
    y1 = window_height-100

    x2 = 200
    y2 = window_height-100

    x3 = 150
    y3 = window_height - 200

    # Fargen til trekantene representert av en tuple med rgb verdier
    # og en alpha verdi, alle trekantene skal ha samme farge.
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)
    cyan = (0, 255, 255, 255)
    white = (255, 255, 255, 255)

    color = cyan

    # Finner bredde og høyde på den originale trekanten
    width = Triangle.get_width(x1, x2, x3)
    height = Triangle.get_height(y1, y2, y3)

    # Henter inn argumentet og gjør det om til int,
    # siden den tolkes som en string
    n = int(sys.argv[1])

    # Lager den første trekanten og legger den inn i den første listen
    triangle_list = []
    triangle = Triangle(x1, y1, x2, y2, x3, y3, canvas)
    triangle_list.append(triangle)


    # Lager sierpinski trekanten av n-te grad
    complete_triangle_list = SierpinskiTriangle.calculate_triangles(width, height, triangle_list, n)

    # Initialiserer sierpinski trekanten
    sierpinski = SierpinskiTriangle(complete_triangle_list, n)

    # Skalerer og forflytter trekanten, kan enkelt endres i funksjonen
    SierpinskiTriangle.orient_triangles(complete_triangle_list, n)

    # Hoved loop for å displaye trekanten
    while running:
        
        # Fyller bakgrunnen med fargen
        canvas.fill(screencolor)

        # Tegner alle trekantene. Trenger strengt tatt ikke
        # være inne i hoved loopen, da de ikke flytter på seg
        for triangle in complete_triangle_list:
            triangle.draw_triangle(color)

        # Oppdaterer display
        pygame.display.update()


        # Event handling, i tilfelle en skal krysser ut programmet etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnign = False
                pygame.display.quit()
                pygame.quit()

if __name__ == '__main__':
    main()