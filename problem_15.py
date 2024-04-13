# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calculate the central binomial coefficient
routes = factorial(40) // (factorial(20) * factorial(20))

print("Number of routes through a 20 x 20 grid:", routes)
