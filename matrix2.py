### Count how many 0 in matrix
matrix = [[0,5,1],
          [4,9,0],
          [1,6,0]]

#print(matrix[1][1])

counter = 0
for i in range(len(matrix)): ### read rows
    for j in range(len(matrix)): ### read columns
        if matrix[i][j] == 0:
            counter += 1
print(counter)    
        #print(matrix[i][j]*2, end = " ")
    #print() 