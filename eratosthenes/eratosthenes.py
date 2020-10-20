from sys import argv

# Command Line Usage: 
#   python3 eratosthene.py [N]
def main():
    if len(argv) == 1:
        sieve(30)
    else:
        sieve(int(argv[1]))

def sieve(N):
    primes = [0] * (N + 1);
    primes[2] = 1
    for i in range(3, N + 1):
        if (i % 2 == 1):
            primes[i] = 1 

    m = 3
    n = m ** 2
    while n <= N:
        if primes[m] == 1:
            while n <= N:
                primes[n] = 0
                n = n + 2 * m
        m = m + 2
        n = m ** 2

    for k in range(N):
        if primes[k] == 1:
            print(k)

if __name__ == "__main__":
    main()
