# 6. Write a Python program that reads a number and finds the sum of the series of 1 +11 + 111 + 1111 +
# ....+N terms.
# =====================================================
# Sample Input1:
# 5
# Sample Output1:
# 1 + 11 + 111 + 1111 + 11111
# The Sum is: 1234
# =====================================================
# Sample Input2:
# 8
# Sample Output2:
# 1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111
# The Sum is: 12345678
# ====================================================


num=int(input("Enter a number :"))
s=0
sum1=0
print("")
for i in range(0, num):
    s = s * 10 + 1
    sum1 += s
    print(s, end=" ")
    
print()
print("The Sum is:", sum1)