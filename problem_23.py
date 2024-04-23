def find_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_abundant(n):
    return sum(find_divisors(n)) > n

def find_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(12, limit):
        if is_abundant(i):
            abundant_numbers.append(i)
    return abundant_numbers

def find_non_abundant_sum(limit):
    abundant_numbers = find_abundant_numbers(limit)
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])
    non_abundant_sum = 0
    for i in range(1, limit):
        if i not in abundant_sums:
            non_abundant_sum += i
    return non_abundant_sum, abundant_numbers
arr=[]
limit = 28123
(result, arr) = find_non_abundant_sum(limit)
print("The sum of all positive integers which cannot be written as the sum of two abundant numbers is:", result)
print(arr)