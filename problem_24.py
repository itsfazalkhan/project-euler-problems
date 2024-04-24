def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def find_lexicographic_permutation():
    millionth = 1000000
    digits = list(range(10))
    permutation = ""
    
    for i in range(9, -1, -1):
        index = (millionth - 1) // factorial(i)
        permutation += str(digits[index])
        digits.pop(index)
        millionth -= index * factorial(i)
    
    return permutation

result = find_lexicographic_permutation()
print("The millionth lexicographic permutation of the digits 0 to 9 is:", result)
