import numpy as np
def solution(a):
	a = np.array(a)
	return a[..., -1:]
