def number_to_words(n):
    if n == 1000:
        return "one thousand"
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    words = ""
    
    hundreds_digit = n // 100
    tens_digit = (n % 100) // 10
    ones_digit = n % 10
    
    if hundreds_digit > 0:
        words += ones[hundreds_digit] + " hundred"
        if tens_digit > 0 or ones_digit > 0:
            words += " and "
    
    if tens_digit == 1:
        words += teens[ones_digit]
    else:
        words += tens[tens_digit]
        words += " " + ones[ones_digit]
    
    return words.strip()

def count_letters_in_numbers(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        words = number_to_words(i)
        # Count letters and remove spaces and hyphens
        letters = len(words.replace(" ", "").replace("-", ""))
        total_letters += letters
    return total_letters

# Test
total_letters = count_letters_in_numbers(1000)
print("Total letters used:", total_letters)
