import numpy as np

n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

arr = np.zeros((5,50))

for i in range(5):
	for j in range(50):
		if j < n1[i]:
			arr[i][j] = 0
		elif j >= n2[i]:
			arr[i][j] = 30
