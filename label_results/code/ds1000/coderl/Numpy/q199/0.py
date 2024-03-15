import numpy as np
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]
arr = (np.random.rand(5,50)-0.5) * 50

for i in range(0,len(n1)):
	temp_arr = arr.copy()
	mask = temp_arr < n1[i]
	temp_arr[mask] = 0
	arr[temp_arr] = arr[temp_arr] + 5

for i in range(0,len(n2)):
	temp_arr = arr.copy()
	mask = temp_arr < n2[i]
	temp_arr[mask] = 0
	arr[temp_arr] = arr[temp_arr] + 5
