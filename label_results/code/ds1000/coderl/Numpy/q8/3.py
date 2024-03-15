import numpy as np
a = np.array([[1,0,3], [2,4,1]])
b = np.array([[0,1,0,0,0], [1,0,0,0,0], [0,0,0,1,0], [0,0,1,0,0], [0,0,0,0,1], [0,1,0,0,0]])
for i in range(len(b)):
	a_i = a[i, :]
	b_i = b[i, :]
	for j in range(len(a_i)):
		if a_i[j] == b_i[j]:
			b_i[j] = 1 - b_i[j]
