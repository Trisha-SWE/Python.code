# #n = int(input("Enter a number: "))

# i = 1

# while i <= n:
#     print(i, end="")
#     i = i + 1

# i = n - 1

# while i >= 1:
#     print(i, end="")
#    i = i - 1



# Read input number
n = int(input("Enter a number (1-9): "))

# Generate ascending part
for i in range(1, n + 1):
    print(i, end="")

# Generate descending part
for i in range(n - 1, 0, -1):
    print(i, end="")

print() # For new line
