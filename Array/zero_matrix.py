def zero_matrix(matrix):
    list_row = []
    list_col = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i not in list_row:
                    list_row.append(i)

                if j not in list_col:
                    list_col.append(j)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in list_row or j in list_col:
                matrix[i][j] = 0
    
    return matrix

matrix = [[1,1,1,0],
          [1,0,1,1],
          [1,1,1,1],
          [1,1,0,1]]
print("Before: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = " ")
    print()

matrix = zero_matrix(matrix)
print()
print("Afer: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = " ")
    print()