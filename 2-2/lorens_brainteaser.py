list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]

for i in list_of_lists:
    for j in i:
        print(j, end=" ")

list_of_lists_2 = [[3,2,1], [6,5,4], [9,8,7]]

for i in list_of_lists_2:
    for j in reversed(i):
        print(j, end=" ")