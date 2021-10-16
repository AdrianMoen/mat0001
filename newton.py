# Author: Adrian Løberg Moen
# Github: AdrianMoen
# Email: Adrian.Moen01@gmail.com
# Orker ikke en objekt orientert implementasjon for denne heller
import sys
import math

# Funksjon som regner ut iht. funksjonen
def function(x):

    originalTestFunction = pow(x,3)-5*x-3

    return x*(math.e**x)-1


# Vi antar at funksjonen er statisk, derfor har jeg ingen funksjon som regner ut den deriverte
def derivative(x):

    originalTestFunction = 3*pow(x,2)-5

    return (math.e**x)*x + math.e**x


# Utfører newtons metode rekursivt
def newtonsMethod(start, n, p):

    # regner ut x_n+1 = x_n - f(x)/f'(x)
    XsubN = start - (function(start)/derivative(start))

    # Når vi når enden, returnerer vi. Dersom n = 0, skal vi returnere start verdien
    if p >= n:
        if n != 0:
            return XsubN
        else:
            return start
    
    p += 1

    # Kaller på seg selv på nytt men med XsubN som argument
    return newtonsMethod(XsubN, n, p)


def main():
    '''
                            Første del er error handling i tilfelle programmet brukes feil
    int Start               henter argument nr 1, som er start x verdien
    int n                   henger n, som angir antall iterasjoner
    int p                   teller for antal iterasjoner som er tatt
    float approxZeroValue   henter resultatet fra newtons metode med argumentene @start, @n, @p
    '''

    # Error handling i tilfelle noen starter programmet feil osv
    if len(sys.argv) == 1:
        print("\033[91m ERROR: missing arguments, how to use: newton.py [x] [n] \033[0m")
        return 0
    try:
        assert type(int(sys.argv[1])) == int
        assert type(int(sys.argv[2])) == int
    except:
        print("\033[91m ERROR: arguments must be integers, how to use: newton.py [x] [n] \033[0m ")
        return 0

    # Henter start vediene
    start = int(sys.argv[1])
    n = int(sys.argv[2])

    # Startet på iterasjon 1
    p = 1

    # Henter approximated zero value ved bruk av newtons metode
    approxZeroValue = newtonsMethod(start, n, p)
    
    print("newtons method:")
    print("approximated zero value: ", approxZeroValue)


if __name__ == '__main__':
    main()