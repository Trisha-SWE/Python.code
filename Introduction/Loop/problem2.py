# 2. Read the value N from the user, and print the first Nth Fibonacci numbers.
# Sample Input:
# 9
# Output:
# 0 1 1 2 3 5 8 13 21

# Sample Input:
# 5
# Output:
# 0 1 1 2 3

# Take input from the user

n = int(input("Enter how many Fibonacci numbers: "))

first = 0
second = 1

for i in range(n):
    print(first, end=" ")

    next = first + second
    first = second
    second = next