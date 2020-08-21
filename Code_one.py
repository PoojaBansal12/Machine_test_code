
n = input("Enter the number of Row and Column as row,column: ")
row,col=0,0
multi_list=[]
try:
    row = n.split(",")[0]
    col = n.split(",")[1]
    multi_list = [[0 for col_num in range(int(col))] for row_num in range(int(row))]
except:
    print("Please enter the number of row and column in proper format.")
    exit(0)



print("Enter the elements: ")
try:
    for i in range(int(row)):
        for j in range(int(col)):
            multi_list[i][j] = int(input())
    print(multi_list)
except:
    print('invalid element added')




