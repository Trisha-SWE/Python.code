num_string = input("The list: ")
num_list = num_string[1:len(num_string)-1].split(",")
print(num_list)

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

for i in num_list:
    if i % 2 == 0:
        print("1st Even:", i)
        break

for i in num_list:
    if i % 2 != 0:
        print("1st Odd:", i)
        break