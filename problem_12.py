def div_count(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 2
    return count

def findTriangle(threshold):
    tri_num = 1
    n = 1
    while True:
        if n % 2 == 0:
            tri_num = n * (n // 2 + 1)
        else:
            tri_num = (n + 1) * (n // 2 + 1)
        divs = div_count(tri_num)
        if divs > threshold:
            return tri_num
        n += 1

result = findTriangle(500)
print(result)