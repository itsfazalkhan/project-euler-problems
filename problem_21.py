def sum_of_divisors(n):
    divisor_sum = 1  # Start with 1 as it's always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # If not a perfect square, add the other divisor
                divisor_sum += n // i
    return divisor_sum

def sum_of_amicable_numbers(limit):
    amicable_sum = 0
    for a in range(2, limit):
        b = sum_of_divisors(a)
        if b > a and sum_of_divisors(b) == a:  # Check for amicable pair
            amicable_sum += a + b
    return amicable_sum

result = sum_of_amicable_numbers(10000)
print("The sum of all amicable numbers under 10000 is:", result)
