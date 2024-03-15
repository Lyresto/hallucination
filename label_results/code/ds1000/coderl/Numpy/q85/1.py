import numpy as np

def generate_array(n, one_ratio=0.9):
	num = np.random.randint(2, size=n)
	ones_per_num = int(1 - one_ratio * num)
	return [0 if i == randomLabel else 1 for i in range(n)]
