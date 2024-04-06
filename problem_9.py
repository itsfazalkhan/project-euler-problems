'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2+b^2=c^2
    For example, 3^2 + 4^2
    9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c=1000
Find the product abc.'''

def pythagoreanTriplet(sum_of_triplet):
    for a in range(1, sum_of_triplet//3):
        for b in range(a, sum_of_triplet//2):
            c = sum_of_triplet - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
n=1000
a, b, c = pythagoreanTriplet(n)
product = a * b * c
print("The Pythagorean triplet is:", a, b, c)
print("The product of the triplet abc is:", product)