# 5. Write a python function that takes a string with multiple numbers separated by commas as input from
# the user. Extract the numbers from the string and make a list and print it. Multiply the numbers of the
# list and print the product. [Hint: You can use split()]
# =====================================================
# Sample Input1:
# 1,2,3,4,5
# Sample output1:
# ['1', '2', '3', '4', '5']
# Product:120
# =====================================================
# Sample Input2:
# 10,0,20,3,1
# Sample Output2:
# ['10', '0', '20', '3', '1']
# Product:0


values = input("Enter number separated by commas: ")

useList = values.split(",")
print(useList)