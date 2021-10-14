# Author: Adrian Løberg Moen
# Github: AdrianMoen
# Email: Adrian.Moen01@gmail.com
import sys
import math
import pygame
import pygame.gfxdraw
from pygame import color
from pygame.locals import *

pygame.init()
pygame.font.init()

# Vindus dimensjoner
window_width = 1280
window_height = 720

# Skjerm bakgrunnsfarge
screencolor = (0, 0, 0)

# Setter opp pygame sin display og ett canvas, samt en tekstfont
canvas = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sierpinski trekant")
textFont = pygame.font.SysFont("calibri", 30, bold=False, italic=False)


class Triangle():
    '''
    Håndterer selve trekanten. siden alle trekantene er et eget objekt
    Functions:
        __init__()          Initialiserer trekanten, tilegner den en surface, og koordinater
        draw_triangle()     Tegner trekanten, blir kalt en gang for hver trekant for hver "frame"
        get_length()        Regner ut lengden på trekanten, alle sidene er like lange
    '''
    def __init__(self, x1, y1, x2, y2, x3, y3, surface):
        self.x1 = x1
        self.y1 = y1
        
        self.x2 = x2
        self.y2 = y2
        
        self.x3 = x3
        self.y3 = y3
        
        self.surface = surface

    # Tegner selve trekanten ved bruk av gfxdraw, en kan også ender det til filled_trigon()
    def draw_triangle(self, color, filled):
        
        if filled == 1:
            pygame.gfxdraw.filled_trigon(self.surface, int(self.x1), int(self.y1), int(self.x2), int(self.y2), int(self.x3), int(self.y3), color)
        else:
            pygame.gfxdraw.trigon(self.surface, int(self.x1), int(self.y1), int(self.x2), int(self.y2), int(self.x3), int(self.y3), color)


    # Finner, og returnerer lengden på trekanten, valget av x istedenfor y er helt vilkårlig
    def get_length(self):
        
        width = self.x2 - self.x1

        return width



# Gjør sierpinksi delen om til en klasse, mest for at det skal se pent ut
class SierpinskiTriangle():
    '''
    Denne klassen brukes for alt relatert til Sierpinski trekanten, dvs trekantene som en enhet.
    Functions: 
        __init__                Initialiserer trekanten, tilegner den en n og lengde (lengden på den endelige trekanten)
        calculate_triangles()   Tar inn en liste med trekanter, multipliserer den n ganger slik som
                                Sierpinksitrekanten skal se ut, og returnerer en fullstending liste med alle trekantene
        orient_triangle()       Tar listen med trekantene, skalerer, og sentrerer trekanten
        find_area()             Finner arealet av alle de tegnede trekantene
        find_circumference()    Finner omkretsen av alle de tegnede trekantene
        find_xmax               Finner største x verdi, høyre kant, i sierpinski trekanten
        find_xmin               Finner minste x verdi, venstre kant, i sierpinksi trekanten
        find_ymax               Finner største y verdi, nederste punkt, på sierpinski trekanten
    '''
    def __init__(self, n, length):
        self.n = n
        self.length = length



    # Rekursiv funksjon som produserer en liste med alle trekantene
    def calculate_triangles(self, triangle_list):
        
        # Ny liste for å lagre de nye trekantene som skal videre i rekursjonen
        new_triangle_list = []

        # Sjekker om vi har nådd n-te iterasjon
        if self.n <= 1:
            return triangle_list

        # Lager trekanten som forflyttes til høyre og legges til i den nye lista
        for triangle in triangle_list:
            x1New = triangle.x1 + self.length
            x2New = triangle.x2 + self.length
            x3New = triangle.x3 + self.length

            newTriangle = Triangle(x1New, triangle.y1, x2New, triangle.y2, x3New, triangle.y3, canvas)
            # Den "originale" trekanten legges til i den nye lista og blir med videre.
            new_triangle_list.append(newTriangle)
            new_triangle_list.append(triangle)

        # Lager trekanten som forflyttes opp of til høyre i midten, og legger til i den nye lista
        for triangle in triangle_list:
            x1New = triangle.x1 + self.length/2
            x2New = triangle.x2 + self.length/2
            x3New = triangle.x3 + self.length/2
            
            y1New = triangle.y1 - self.length
            y2New = triangle.y2 - self.length
            y3New = triangle.y3 - self.length

            newTriangle = Triangle(x1New, y1New, x2New, y2New, x3New, y3New, canvas)
            new_triangle_list.append(newTriangle)
    
        # Fjerner triangle_list for hver gang, siden en ny sendes videre
        del triangle_list

        # Skalerer trekantens bredde slik at de nestkommende 
        # plasseres riktig
        self.length  *= 2

        # Reduserer n
        self.n = self.n - 1

        # Kaller seg selv rekursivt
        return_list = self.calculate_triangles(new_triangle_list)
        return return_list


    def orient_triangles(self, triangle_list, n):
    
        # Skalerer trekantene, her er 23 et vilkårlig tall slik at trekanten blir en passe størelse
        # Trekantens bredde øker med 2^n, derav deles den på 2^n
        for triangle in triangle_list:
            triangle.x1 = ((triangle.x1*23)/2**(n+1))
            triangle.x2 = ((triangle.x2*23)/2**(n+1))
            triangle.x3 = ((triangle.x3*23)/2**(n+1))

            triangle.y1 = ((triangle.y1*23)/2**(n+1))
            triangle.y2 = ((triangle.y2*23)/2**(n+1))
            triangle.y3 = ((triangle.y3*23)/2**(n+1))

        # trenger min og max x for lengde av den skalerte trekanten, og maxy/minx for sentrering
        minX = self.find_xmin(triangle_list)
        maxX = self.find_xmax(triangle_list)
        maxY = self.find_ymax(triangle_list)

        # Samtlige tall som trengs for å finne moveX og moveY
        # som er forflyttning på x og y aksen
        width = maxX-minX

        startingX = window_width/2 - width/2
        startingY = window_height - 100

        moveX = minX - startingX
        moveY = startingY - maxY

        # Flytter trekanten slik at den blir sentrert
        for triangle in triangle_list:
        
            triangle.x1 -= moveX
            triangle.x2 -= moveX
            triangle.x3 -= moveX
            
            triangle.y1 += moveY
            triangle.y2 += moveY
            triangle.y3 += moveY


    # Finner, og returnerer arealet til trekanten
    def find_area(self, triangle_list):
        
        totalArea = 0
        
        for triangle in triangle_list:
            side = triangle.x3 - triangle.x1

            totalArea += ((math.sqrt(3)/4)*side**2)

        return totalArea


    # Finner, og returner omkretsen til trekanten
    def find_circumference(self, triangle_list):
        
        totalSum = 0

        for triangle in triangle_list:
            length = triangle.x3 - triangle.x1

            totalSum += (length*3)
        
        return totalSum


    # Finner, og returnerer den største x verdien
    def find_xmax(self, triangle_list):
        n = 0
        # Bare x2 kan være størst
        for triangle in triangle_list:

            x2 = triangle.x2
            if n == 0:
                maxX = x2
                n += 1

            if x2 > maxX:
                maxX = x2

        return maxX


    # Finner, og returnerer den minste x verdien
    def find_xmin(self, triangle_list):
        n = 0
        # Bare x1 kan være minst
        for triangle in triangle_list:

            x1 = triangle.x1
            if n == 0:
                minX = x1
                n += 1

            if x1 < minX:
                minX = x1

        return minX


    # Finner og returnerer den minste y verdien
    def find_ymax(self, triangle_list):
        n = 0
        # y1 og y2 er altid minst, siden det er en likesidet trekant. 
        # valget av y1 er helt vilkårlig
        for triangle in triangle_list:

            y1 = triangle.y1
            if n == 0:
                maxY = y1
                n += 1
            
            if y1 > maxY:
                maxY = y1

        return maxY



def main():
    '''
    Hoved del i programmet
    Inneholder:
        Declareringer av viktige verdier og variabler relatert til trekantene
        Alle viktige funksjonskall, initialisering av Sierpinskitrekanten osv.
        Hoved loop skriving til skjerm, og holde skjermen og programmet oppe (main engine)
    '''
    # Mens denne er sann, vill hoved loopen kjøre
    running = True

    # posisjon til den første trekanten, relativ posisjon er vilkårlig
    x1 = 100
    y1 = window_height-100

    x2 = 200
    y2 = window_height-100

    x3 = 150
    y3 = window_height - 200

    # Fargen til trekantene representert av en tuple med rgb verdier
    # og en alpha verdi, alle trekantene får samme farge.
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)
    cyan = (0, 255, 255, 255)
    white = (255, 255, 255, 255)

    color = cyan

    # Henter inn argumentet og gjør det om til int
    # Dersom ingen argument, eller ikke heltall, printes en feilmelding
    try:
        n = int(sys.argv[1])
    except:
        print('\033[91m' + "ERROR: no n'th degree given, formula for running: SierpinskiTriangle.py [n] [optional]:[\"filled\"]" + '\033[0m')
        print('\033[93m' + "WARNING: note that n should also be an integer, preferably not bigger than 14" + '\033[0m')
        return 0

    # Dersom argv nr 2 er: "filled", blir trekanten fyllt, ellers, blir den ikke det
    try:
        if sys.argv[2] == "filled":
            filled = 1
    except:
        filled = 0


    # Lager den første trekanten og legger den inn i den første listen
    triangle_list = []
    triangle = Triangle(x1, y1, x2, y2, x3, y3, canvas)
    triangle_list.append(triangle)

    # Finner bredde og høyde på den originale trekanten
    length = triangle.get_length()

    # Initialiserer sierpinski trekanten med grad n
    sierpinski = SierpinskiTriangle(n, length)
    
    # Lager sierpinski trekanten, skalerer og forflytter den
    complete_triangle_list = sierpinski.calculate_triangles(triangle_list)
    sierpinski.orient_triangles(complete_triangle_list, n)
    
    # Finner arealet og omkretsen
    totalArea = sierpinski.find_area(complete_triangle_list)
    totalCircumference = sierpinski.find_circumference(complete_triangle_list)

    # Hoved loop
    while running:  
        
        # Fyller bakgrunnen med fargen
        canvas.fill(screencolor)

        # Tegner alle trekantene
        for triangle in complete_triangle_list:
            triangle.draw_triangle(color, filled)

        # Tegner teksten, og 'bliter' den på bakgrunnen
        header = textFont.render("Arealet og omkretsen ved %d-te grad" % n, False, (255, 255, 255))
        area = textFont.render("A = %d" % totalArea, False, (255, 255, 255))
        circumference = textFont.render("O = %d" % totalCircumference, False, (255, 255, 255))

        canvas.blit(header,(100, 100))
        canvas.blit(area, (100, 130))
        canvas.blit(circumference, (100, 160))

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