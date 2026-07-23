numbers = input("Enter numbers: ").split()

nums = []

for x in numbers:
    nums.append(int(x))

first_even = "not found"
first_odd = "not found"
last_even = "not found"
last_odd = "not found"

for num in nums:

    if first_even == "not found" and num % 2 == 0:
        first_even = num

    if first_odd == "not found" and num % 2 != 0:
        first_odd = num

    if num % 2 == 0:
        last_even = num
    else:
        last_odd = num

print("First even:", first_even)
print("First odd:", first_odd)
print("Last even:", last_even)
print("Last odd:", last_odd)