# 4. Write a Python program to Capitalize the first character of each word in a String [You cannot use the
# built-in upper() function]
# Sample Input:
# I love python programming
# Sample Output:
# I Love Python Programming

str=input("Enter a string:")
words=str.split()
for i in range(len(words)):
    words[i]=words[i][0].upper()+words[i][1:]
print(" ".join(words))
