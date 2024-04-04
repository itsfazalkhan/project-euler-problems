def sum_of_squares(n):
    # Calculate the sum of the squares of the first n natural numbers
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    # Calculate the square of the sum of the first n natural numbers
    return sum(range(1, n+1))**2

def difference(n):
    # Find the difference between the square of the sum and the sum of the squares
    x=square_of_sum(n)
    y=sum_of_squares(n)
    return x,y,x-y

# Find the difference for the first one hundred natural numbers
(x,y,result) = difference(100)
print(f"{x}-{y} =", result)