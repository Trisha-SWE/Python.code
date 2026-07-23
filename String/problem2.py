# 2. Write a Python program to find the largest and smallest word in a string.
# [you are not allowed to use max() and min()]
# Sample Input :
# It is a string with the smallest and largest word.
# Sample Output :
# The largest word is “smallest” and the smallest word is 'a'.


text = input("Enter a sentence: ")

words = text.split()

largest = words[0]
smallest = words[0]


for word in words:

   
    word = word.strip(".")

    if len(word) > len(largest):
        largest = word

    if len(word) < len(smallest):
        smallest = word


print("The largest word is", largest)
print("The smallest word is", smallest)