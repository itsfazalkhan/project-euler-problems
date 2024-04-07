'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
   Find the sum of all the primes below two million.'''

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]

def sum_of_primes_below_n(n):
    primes = sieve(n)
    return sum(primes)

n = 2000000
result = sum_of_primes_below_n(n)
print(result)
