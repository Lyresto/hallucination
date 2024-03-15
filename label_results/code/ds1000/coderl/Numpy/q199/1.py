import numpy as np

n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

mask = np.array(n1) < n2
arr[mask] = 0

for i in range(n2.size):
	arr[(mask & (i==0))] = 30

