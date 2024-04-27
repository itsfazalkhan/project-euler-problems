def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_consecutive_primes(a, b):
    n = 0
    while True:
        value = n * n + a * n + b
        if not is_prime(value):
            break
        n += 1
    return n

def find_max_product(a_range, b_range):
    max_consecutive_primes = 0
    product = 0

    for a in range(*a_range):
        for b in range(*b_range):
            consecutive = count_consecutive_primes(a, b)
            if consecutive > max_consecutive_primes:
                max_consecutive_primes = consecutive
                product = a * b

    return product

def main():
    a_range = (-999, 1000)
    b_range = (-1000, 1001)
    product = find_max_product(a_range, b_range)
    print("Product of coefficients:", product)

if __name__ == "__main__":
    main()
