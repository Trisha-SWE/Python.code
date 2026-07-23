# 1. Write a Python program to count the total number of alphabets, digits, and special characters in a string.
# Here, space is considered as a special character.
# ====================================================
# Sample Input:
# This is CSE110 Course.
# Sample Output:
# The number of Alphabets in the string is: 15
# The number of Digits in the string is : 3
# The number of Special characters in the string is: 4




text = input("Enter a string: ")

alphabet = 0
digit = 0
special = 0

for ch in text:

    if ch.isalpha():
        alphabet += 1

    elif ch.isdigit():
        digit += 1

    else:
        special += 1

print("The number of Alphabets in the string is:", alphabet)
print("The number of Digits in the string is:", digit)
print("The number of Special characters in the string is:", special)