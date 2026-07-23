# 3. Write a Python program that takes two strings from the user. Then remove characters from the first
# string which are present in the second string. [you are not allowed to use replace() ]
# =====================================================
# Sample Input1:
# India is great
# is
# Sample Output1:
# nda great
# =====================================================
# Sample Input2:
# this is cSe110 course and we love it
# lo1iva
# Sample Output2:
# ths s cse0 curse nd we e t
# =====================================================
# Sample Input3:
# next course is cse111
# lo1iva
# Sample Output3:
# ext coure i ce111

# str=input("Enter a string: ")
# str2=input("Enter another string: ")

# for char in str2:
#     str=str.replace(char, "")

# print(str)


text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

result = ""

for ch in text1:

    if ch.lower() not in text2.lower():
        result += ch

print(result)