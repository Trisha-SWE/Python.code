# 4. Write a function in Python that will take a number string text as input from the user and returns a
# dictionary having the unique numbers as the keys and the tuple of being the number to be even, odd,
# prime and perfect as thevalues.
# ==================================================
# Hints (1): Write a function to check whether a number is Perfect or not and RETURN “Perfect” and “Not
# Perfect” accordingly.
# Hints (2): Write a function to check whether a number is Prime or not and RETURN “Prime” and “Not
# Prime” accordingly.
# Hints (3): Write a function to check whether a number is Even or not and RETURN “Even” and “Odd”
# accordingly.
# Hints (4): Call 3 above mentioned functions and store their returned values in a list/tuple.
# even= even_check()
# prime= prime_check()
# perfect= perfect_check()
# tup_for_digit = (even, prime, perfect)
# ==================================================
# Sample Input1:
# "2441396"
# Function Call1:
# function_name("2441396")
# Sample Output1:
# {2: ('even', 'prime', 'not perfect'), 4: ('even', 'not prime', 'not perfect'), 1: ('odd', 'not
# prime', 'not perfect'), 3: ('odd', 'prime', 'not perfect'), 9: ('odd', 'not prime', 'not perfect'), 6: ('even', 'not
# prime', 'perfect')}
# ==================================================

def even_check(num):

    if num % 2 == 0:
        return "even"
    else:
        return "odd"


def prime_check(num):

    if num < 2:
        return "not prime"

    for i in range(2, num):
        if num % i == 0:
            return "not prime"

    return "prime"


def perfect_check(num):

    total = 0

    for i in range(1, num):

        if num % i == 0:
            total = total + i

    if total == num:
        return "perfect"
    else:
        return "not perfect"


def number_information(text):

    result = {}

    for ch in text:

        num = int(ch)

        if num not in result:

            even = even_check(num)
            prime = prime_check(num)
            perfect = perfect_check(num)

            result[num] = (even, prime, perfect)

    return result


text = input("Enter number string: ")

print(number_information(text))