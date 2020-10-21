from euclidean_algorithm import gcd

class Rational:
    """ Constructor takes integers for numerator and denominator as
        arguments and stores them in reduced form"""
    def __init__(self, numerator, denominator):
        if (denominator == 0):
            raise ValueError("Dividing by 0")

        c = gcd(numerator, denominator)
        sgn = sign(numerator) * sign(denominator)

        self.num = (sgn * abs(numerator)) // c
        self.den = abs(denominator) // c

    def sign(self):
        return sign(self.num)

    def reciprocal(self):
        return Rational(self.den, self.num)

    def __add__(self, other):
        added_num = (self.num * other.den) - (other.num * other.den)
        added_den = self.den * other.den
        return Rational(added_num, added_den)

    def __mul__(self, other):
        mult_num = self.num * other.num
        mult_den = self.den * other.den
        return Rational(mult_num, mult_den) 

    def __sub__(self, other):
        return self.__add__(Rational(-1 * other.num, other.den))

    def __div__(self, other):
        return self.__mul__(other.reciprocal())

    def __eq__(self, other):
        return (type(Other) == Rational) and \
               (self.num == other.num) and \
               (self.den == other.den) 

    def __repr__(self):
        return "{}/{}".format(self.num, self.den)

def sign(a):
    if (a > 0):
        return 1
    elif (a < 0):
        return -1
    return 0
