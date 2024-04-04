'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

def is_prime(number):
    if number < 2:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # If number is divisible by any number other than 1 and itself, it's not prime
    return True

def find_10001st_prime():
    count = 0
    number = 2
    while True:
        if is_prime(number):
            count += 1
            if count == 10001:
                return number
        number += 1

# Finding the 10,001st prime number
prime_10001 = find_10001st_prime()

print("The 10,001st prime number is:", prime_10001)