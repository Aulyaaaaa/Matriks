def divide_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
	row = []
	for j in range(len(matrix1[0])):
	    row.append(matrix1[i][j] / matrix2[i][j])

	result.append(row)
     return result
