import math

def eratostenes(n):
            sieve = [
            True for _ in range(n + 1)]
            for i in range(2, math.ceil(math.sqrt(n))):
                        if sieve[i]:
                            for j in range(2 * i, n + 1, i):
                                    sieve[j] = False
            primes = []
            for i in range(2, n + 1):
                    if sieve[i]:
                        primes.append(i)
            return primes

n = 137
primes = eratostenes(n)
print('[DEBUG] liczby pierwsze od 2 do {}:'.format(n))
print('[DEBUG]', ', '.join(map(str, primes)))
