choice = input("Enter True or False: ")
n = 9
row = 5
if choice.lower() == "true":
    for x in range(row):
        print(' ' * (n - x - 1) + '*' * (2 * x + 1))
elif choice.lower() == "false":

    for i in range(row, 0, -1):
        for j in range(row - i):
            print(' ', end='')  # printing space and staying in same line

        for j in range(2 * i - 1):
            print('*', end='')  # printing * and staying in same line
        print()  # printing new line
else:
    print("Invalid input")