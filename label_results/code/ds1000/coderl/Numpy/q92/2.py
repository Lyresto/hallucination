import numpy as np

def sort_it(a):
	m = -1
	res = []
	for i in range(len(a)):
		if a[i] > m:
			m = a[i]
			res = [i]
		elif a[i] == m:
			res.append(i)
	return res


# in the end, you know that the indices of the N biggest elements in decreasing order should give (considering N = 3)
