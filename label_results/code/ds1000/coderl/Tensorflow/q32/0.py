import numpy as np


def find_space_average(x):
	s = np.mean(np.array(x[0][0]), axis=-1)
	nz = len([i for i in x[0][0] if i!= 0])
	return [s / nz for i in range(len(s))]
