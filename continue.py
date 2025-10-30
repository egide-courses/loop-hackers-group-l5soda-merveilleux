for num in range(1, 101):
    if num % 3 == 0:
        continue      # skip numbers divisible by 3
    if num == 73:
        break          # stop the loop when number is 73
    print(num)
