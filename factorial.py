n = int(input("Enter a number: "))

fact = 1   # start with 1

for i in range(1, n + 1):
    fact = fact * i   # multiply each number

print("The factorial of", n, "is", fact)
