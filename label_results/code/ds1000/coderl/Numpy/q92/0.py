import numpy as np
a = np.array([4, 1, 0, 8, 5, 2])
N = 3
def get_result(N):
	arr = np.array(a)
	index_list = []
	for i in range(len(arr)):
		if (i == N-1):
			index_list.append(i)
		elif arr[i] > arr[i+1]:
			index_list.append(i)
	return index_list
