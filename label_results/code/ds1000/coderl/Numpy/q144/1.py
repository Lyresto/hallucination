import numpy as np

def zero_out_first_and_second(a):
	for i in range(len(a)):
		for j in range(len(a[0])):
			a[i][j] = a[i][0] if a[i][0]!= 0 else 0
	for j in range(len(a[0])):
		a[0][j] = a[0][j] if a[0][j]!= 0 else 0
