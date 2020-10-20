def square_root(n):
    root = n / 2
    for k in range(20):
        root = 0.5 * (root + n / root)
    return root
print(square_root(4))
print(square_root(2))
print(square_root(496))
