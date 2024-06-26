'''Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?'''

def largest_prime_factor(n):
    i = 2
    while i * i <=n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is", result)
