def transpose(matrix):
	new_matrix = []
	for i in range(len(matrix[0])):
		new_matrix.append([matrix[j][i] for j in range(len(matrix))])
	return new_matrix
