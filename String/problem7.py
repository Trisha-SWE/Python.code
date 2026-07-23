# 7. Write a Python program that reads a number and displays the multiplication table of the given integer.
# Sample Input: 15
# Sample Output :
# 15X1=15
# 15X2=30
# ...
# ...
# 15X10=150


# Take input
number = int(input("Enter a number: "))

# Print multiplication table
for i in range(1, 11):
    print(number, "X", i, "=", number * i, sep="")


