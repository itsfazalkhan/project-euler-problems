def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def main():
    n = 100
    fact = factorial(n)
    digit_sum = sum_of_digits(fact)
    print("The sum of the digits in 100! is:", digit_sum)

if __name__ == "__main__":
    main()
