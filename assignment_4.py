# Defining a dictionary with numbers and their word equivalents
d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
     19: 'nineteen', 20: 'twenty',
     30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
     70: 'seventy', 80: 'eighty', 90: 'ninety'}
# Setting limits 
k = 1000
m = k * 1000

def number2words(n):

    assert (0 <= n)

# Handle numbers less than 20
    if (n < 20):
        return d[n]

# Handle numbers between 20 and 99
    if (n < 100):
        if n % 10 == 0:
            return d[n]
        else:
            return d[n // 10 * 10] + '-' + d[n % 10]

# Handle numbers between 100 and 999
    if (n < k):
        if n % 100 == 0:
            return d[n // 100] + ' hundred'
        else:
            return d[n // 100] + ' hundred ' + number2words(n % 100)

# Handle numbers between 1000 and 999,999
    if (n < m):
        if n % k == 0:
            return number2words(n // k) + ' thousand'
        else:
            return number2words(n // k) + ' thousand ' + number2words(n % k)

# Raise an error if the number is too large
    raise AssertionError('n is too large: %s' % str(n))

# Get user input
number_str = input("Enter a number (between 0 and 1 million): ")
number = int(number_str)  # Convert to number 

# Call the function and print the result
words = number2words(number)
print(words)