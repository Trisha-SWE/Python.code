# 3. Read the value of n from the user and compute the value of the following series:
# result = (1**1)/1 + (2**2)/2 + (3**3)/3 + (4**4)/4 + ...... +(n**n)/n
# (Here, ** indicates power)
# ===========================================================
# Sample Input: 3
# Output: 12
# ===========================================================
# Sample Input: 5
# Output: 701

n = int(input("Enter the value of n: "))
result = 0
for i in range(1, n + 1):
    result += (i ** i) / i
print("The value of the series is:", result)