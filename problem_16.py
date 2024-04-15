def sum_of_digits_power_of_2(exp):
    # Calculate 2 raised to the given exponent
    num = 2 ** exp
    
    # Initialize the sum of digits
    digit_sum = 0
    
    # Extract each digit and add it to the sum
    while num > 0:
        digit_sum += num % 10
        num //= 10
    
    return digit_sum

# Calculate the sum of digits of 2^1000
digit_sum = sum_of_digits_power_of_2(1000)
print("The sum of the digits of 2^1000 is:", digit_sum)
