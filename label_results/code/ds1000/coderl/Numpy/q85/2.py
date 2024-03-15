import numpy as np
from itertools import compress

def gen():
	random_label = np.random.randint(2, size=numbers)
	for i in range(0, numbers):
		if random_label[i] == 0:
			yield 0
		else:
			yield 1

nums = list(compress(gen(), [int(one_ratio * size) for one_ratio in range(0, 1.1)]))
