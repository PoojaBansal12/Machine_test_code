try:
    number = int(input("Enter the number of elements you want in the list: "))
    print("Enter the first list elements: ")
    list_one = []
    for i in range(number):
        element = input()
        list_one.append(element)

    print("Enter the second list elements: ")
    list_two = []
    for i in range(number):
        element = input()
        list_two.append(element)

    print(list_one)
    print(list_two)

    result_dict = {list_one[i]: list_two[i] for i in range(len(list_one))}
    print((result_dict))
except:
    print("Invalid Input!")