# Author: Adrian Løberg Moen
# Github: AdrianMoen
# Email: Adrian.Moen01@gmail.com
# Orker ikke en objekt orientert implementasjon for denne
import math

# y er lik hva enn funksjon du skriver inn her, x**n betyr x^n. f. eks brukes math.sqrt(x) for kvadratroter
def function(x):
    y = x * (math.e ** x) - 1
    return y


# Returnerer punktet mellom firstPoint og lastPoint
def find_middle_point(firstPoint, lastPoint):
    return (firstPoint + lastPoint) / 2


# Sjekker om y verdien er positiv eller negativ
def check_sign(x):
    if function(x) > 0:
        sign = "positive"
    elif function(x) < 0:
        sign = "negative"
    else:
        sign = "zero"
    return sign


def bisection(x1, x2, n):

    # Finds middlepoint
    middle = find_middle_point(x1, x2)

    if n <= 0:
        return middle

    # Sjekker for null
    if check_sign(middle) == "zero":
        print("zero point found prematurely: %d", middle)
        return middle

    # Sjekker fortegnene, og fortsetter med rett verdi
    if check_sign(x1) == check_sign(middle):
        return bisection(middle, x2, n - 1)
    elif check_sign(x2) == check_sign(middle):
        return bisection(x1, middle, n - 1)

    print("Something went wrong in the bisection method")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="Find a root in the interval [a, b]")
    parser.add_argument("b", type=int, help="Find a root in the interval [a, b]")
    parser.add_argument("n", type=int, help="Number of iterations")
    args = parser.parse_args()

    approx_zero_value = bisection(args.a, args.b, args.n)

    print("bisection method:")
    print("approximate zero value is:", approx_zero_value)
