num = int(input("Enter an integer: "))

sum_digits = 0

while num > 0:
    digit = num % 10        # get the last digit
    sum_digits = sum_digits + digit
    num = num // 10         # remove the last digit

print("Sum of digits is:", sum_digits)
