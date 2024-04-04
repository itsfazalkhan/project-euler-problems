'''Problem 4: A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 (91 x 99).
Find the largest palindrome made from the product of two 3-digit numbers.'''

import time 
#Function to check if a number is a palindrome'''
def palindrome(n):
    return str(n) == str(n)[::-1]
#Function to find the largest palindrome made from the product of two n-digit numbers
def largest(num_digits):
    a=b=0
    max_num = 10**num_digits - 1
    min_num = 10**(num_digits - 1)
    max_palindrome = 0
    for i in range(max_num, min_num - 1, -1):
        for j in range(max_num, i - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if palindrome(product):
                a=i
                b=j
                max_palindrome = max(max_palindrome, product)
    return a,b,max_palindrome

n = 3
start = time.time()
(a,b,result) = largest(n)
print(f"Largest palindrome product of {n}-digit numbers is {result}")
print(f"{a} x {b} = {result}")  
print(f"{time.time() - start:.2f}s elapsed")