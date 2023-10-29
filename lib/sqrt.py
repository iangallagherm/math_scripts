DEFAULT_STEPS = 20

# Heron's root finding method
def square_root(n, steps = DEFAULT_STEPS):
    root = n / 2
    for k in range(steps):
        root = 0.5 * (root + n / root)
    return root
