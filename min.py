# start by asking for the first number
num = int(input("Enter number 1: "))
maximum = num
minimum = num

# ask for the next 9 numbers
for i in range(2, 11):
    num = int(input("Enter number " + str(i) + ": "))

    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum number is:", maximum)
print("Minimum number is:", minimum)
