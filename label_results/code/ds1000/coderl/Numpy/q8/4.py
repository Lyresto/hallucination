import numpy as np
a = np.array([[1,0,3], [2,4,1]])
b = np.array([[0,1,0,0,0], [1,0,0,0,0], [0,0,0,1,0], [0,0,1,0,0], [0,0,0,0,1], [0,1,0,0,0]])
for row in range(len(a)):
	for col in range(len(a[0])):
		if a[row][col] == b[row][col]:
			a[row][col] = 1-a[row][col]
