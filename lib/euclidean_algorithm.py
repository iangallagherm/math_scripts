""" Computes the gcd of two integers a and b """
def gcd(a, b):

    while b != 0:
        t = b
        b = a mod b
        a = t
    return a

""" Takes two integers a and b and computes values which satisfy
    Bezout's identity.
    
    Returns:
        list [r, s, gcd(a, b)] where r,s are such that
        r*a + s*b gcd(a, b)

    NEED TO IMPLEMENT
"""
def bezout(a, b):
    return
