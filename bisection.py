# Author: Adrian Løberg Moen
# Github: AdrianMoen
# Email: Adrian.Moen01@gmail.com
# Orker ikke en objekt orientert implementasjon for denne
import sys
import math

# y er lik hva enn funksjon du skriver inn her, x**n betyr x^n. f. eks brukes math.sqrt(x) for kvadratroter
def function(x):

    y = x*(math.e**x)-1
    return y


# Returnerer punktet mellom firstPoint og lastPoint
def findMiddlePoint(firstPoint, lastPoint):
    return firstPoint/2 + lastPoint/2


# Sjekker om y verdien er positiv eller negativ
def checkSign(x):
    if function(x) > 0:
        sign = 'positive'
    elif function(x) < 0:
        sign = 'negative'
    else:
        sign = 'zero'
    return sign


def bisectionMethod(x1, x2, n):

    # Finds middlepoint
    middleX = findMiddlePoint(x1, x2)

    if n <= 0:
        return middleX

    # Sjekker for null
    if checkSign(middleX) == 'zero':
        print("zero point found prematurely: %d", middleX)
        return middleX
    
    # Sjekker fortegnene, og fortsetter med rett verdi
    if checkSign(x1) == checkSign(middleX):
        n -= 1
        return bisectionMethod(middleX, x2, n)
    elif checkSign(x2) == checkSign(middleX):
        n -= 1
        return bisectionMethod(x1, middleX, n)
    else:
        print("Something went wrong in the bisection method")
        return None


def main():

    # Error handling i tilfelle noen starter programmet feil
    if len(sys.argv) == 1:
        print("\033[91m ERROR: missing arguments, how to use: bisection.py [x1] [x2] [n]\033[0m")
        return 0
    try:
        assert type(int(sys.argv[1])) == int 
        assert type(int(sys.argv[2])) == int
        assert type(int(sys.argv[3])) == int
    except:
        print("\033[91m ERROR: arguments can only integers, how to use: bisection.py [x1] [x2] [n]\033[0m")
        return 0

    start = int(sys.argv[1])
    lastPoint = int(sys.argv[2])
    n = int(sys.argv[3])

    firstPoint = function(start)

    approxZeroValue = bisectionMethod(firstPoint, lastPoint, n)
    
    print("bisection method:")
    print("approxiamate zero value is:", approxZeroValue)


if __name__ == '__main__':
    main()  