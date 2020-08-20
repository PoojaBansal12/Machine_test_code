n = input("Enter the row,column: ")
row = n.split(",")[0]
col = n.split(",")[1]

multi_list = [[0 for col_num in range(int(col))] for row_num in range(int(row))]

print(multi_list)

print("Enter the elements: ")
for i in range(int(row)):
    for j in range(int(col)):
        multi_list[i][j] = int(input())
print(multi_list)


