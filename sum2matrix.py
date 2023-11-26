matrix1 = [[0,5,1],
           [4,9,0],
           [0,6,0]]

matrix2 = [[5,5,1],
           [5,8,1],
           [9,2,6]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

for x in result:
    print(x)