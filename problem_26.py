def find_longest_recurring_cycle(limit):
    max_length = 0
    result = 0
    for d in range(2, limit):
        remainders = {}
        remainder = 1 % d
        position = 0
        while remainder != 0 and remainder not in remainders:
            remainders[remainder] = position
            remainder *= 10
            remainder %= d
            position += 1
        if remainder != 0:
            cycle_length = position - remainders[remainder]
            if cycle_length > max_length:
                max_length = cycle_length
                result = d
    return result

limit = 1000
print(find_longest_recurring_cycle(limit))
