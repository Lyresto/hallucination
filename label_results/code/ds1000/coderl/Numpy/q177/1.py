import numpy as np

def sliding_window(a, size, step=1):
	w = np.zeros(size)
	for y in range(len(a)):
		for x in range(len(a[y])):
			x_cur = x - step
			y_cur = y - step
			w[x_cur:y_cur+1,x_cur:y_cur+1] = a[y][x_cur:y_cur+1]
	return w/float(step)
