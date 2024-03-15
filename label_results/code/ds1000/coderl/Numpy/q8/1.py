import numpy as np

def one_hot(i, j):
	return [int(a == j) for a in range(len(a))]

def numpy_generation(a):
	# beware of the fact that we're computing every element in the array and converting it to a one hot string is easy
	for i, row in enumerate(a):
		for j, value in enumerate(row):
			a[i, j] = str(value)
