def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix[i])):
            if (i == j):
                continue

            temp_val = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp_val
    
    for i in range(len(matrix)):
        for j in range(len(matrix)//2):
            temp_val = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix[i]) - j - 1]
            matrix[i][len(matrix[i]) - j - 1] = temp_val
    
    return matrix

matrix = [['a', 'b', 'c'],
          ['d', 'e', 'f'],  
          ['g', 'h', 'i']]

print("Before:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = " ")
    print()

new_matrix = rotate(matrix)

print("\nAfter: ")
for i in range(len(new_matrix)):
    for j in range(len(new_matrix[i])):
        print(new_matrix[i][j], end = " ")
    print()



