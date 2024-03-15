import numpy as np

def randArray(n, ratio):
	x = np.random.randint(2, size=n)
	return [0 if x == i else 1 for i in range(n)]
