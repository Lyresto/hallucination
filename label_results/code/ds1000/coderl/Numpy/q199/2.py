import numpy as np

arr = (np.random.rand(5, 50)-0.5) * 50
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

for i in range(len(n1)):
	arr[arr < n1[i]] = 0

for i in range(len(n2)):
	arr[arr < n2[i]] += 5
