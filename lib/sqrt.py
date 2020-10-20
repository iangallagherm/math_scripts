DEFAULT_STEPS = 20

def square_root(n, steps = DEFAULT_STEPS):
    root = n / 2
    for k in range(steps):
        root = 0.5 * (root + n / root)
    return root
