def find_pythagorean_triplet(sum_of_triplet):
    for a in range(1, sum_of_triplet//3):
        for b in range(a, sum_of_triplet//2):
            c = sum_of_triplet - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
n=1000
a, b, c = find_pythagorean_triplet(n)
product = a * b * c
print("The Pythagorean triplet is:", a, b, c)
print("The product of the triplet abc is:", product)