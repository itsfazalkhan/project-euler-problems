def fibonacci_with_n_digits(n):
    fib_prev = 1
    fib_curr = 1
    index = 2  # Since F_1 and F_2 are already given
    while len(str(fib_curr)) < n:
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
        index += 1
    return index

result = fibonacci_with_n_digits(1000)
print("The index of the first term in the Fibonacci sequence to contain 1000 digits is:", result)
