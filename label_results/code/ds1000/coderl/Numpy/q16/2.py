import numpy as np
def shift(arr, shift):
	n = len(arr[0])
	s = np.array([[np.nan]*n]*n)
	for x in range(len(arr)):
		for y in range(n):
			s[y][x] = arr[y][x]
			s[y][x] = np.nan if s[y][x] == None else s[y][x] + shift[y]
	return s
