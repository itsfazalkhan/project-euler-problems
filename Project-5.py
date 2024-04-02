'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

# Define the range of numbers from 1 to n
n = 20

# Initialize the number to check
num = n

# Iterate until we find the smallest number that is divisible by all numbers from 1 to n
while True:
    # Check if the number is evenly divisible by all numbers from 1 to n
    if all(num % i == 0 for i in range(1, n + 1)):
        print("The smallest positive number divisible by all numbers from 1 to 20 is:", num)
        break
    # Increment the number to check
    num += n

