from rational import Rational

A = Rational(5, 10)
B = Rational(12, 44)
print(Rational(5, 10))
print(Rational(-5, 10))
print(Rational(5, -10))
print(Rational(-5, -10))

print("{} * {} = {}".format(A, B, A * B))
print("{} / {} = {}".format(B, A, B.__div__(A)))

print(Rational(0, 10))
try:
    print(Rational(5, 0))
except:
    print("Divided by Zero :(") 
