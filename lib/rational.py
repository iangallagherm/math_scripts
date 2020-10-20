from euclidean_algorithm import gcd

class Rational:
    """ Constructor takes integers for numerator and denominator as
        arguments and stores them in reduced form"""
    def __init__(self, numerator, denominator):
        if (denominator == 0):
            raise ValueError("Dividing by 0")

        m = gcd(numerator, denominator)
        sign = sign(numerator) * sign(denominator)

        self.num = (sign * abs(numerator)) // m
        self.den = abs(denominator) // n

    def sign(self):
        return sign(self.num)

    def reciprocal(self):
        return Rational(self.den, num.den)

    def __add__(self, other):
        added_num = (self.num * other.den) - (other.num * other.den)
        added_den = self.den * other.den
        return Rational(num, den)

    def __multiply__(self, other):
        mult_num = self.num * other.num
        mult_den = self.den * other.den
        return Rational(mult_num, mult_den) 

    def __subtract__(self, other):
        return self.__add__(Rational(-1 * other.num, other.den))

    def __divide__(self, other):
        return self.__multiply__(reciprocal(other))

def sign(a):
    if (a > 0):
        return 1
    else if (a < 0):
        return -1
    return 0
