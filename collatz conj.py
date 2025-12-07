num = int(input("Enter a number: "))
iterations = 0
while num != 1:
    iterations += 1
    if num % 2 == 0:
        print(f"{num} is even.")
        num = num / 2
        print(f'New value is {num}')
    else:
        print(f"{num} is odd.")
        num = num * 3 + 1
        print(f'New value is {num}')

print("Reached 1, exiting loop. Total iterations:", iterations)