import numpy as np

def dist(x, y):
	for i in range(3):
		yield [i[0]**2 + i[1]**2, i[2]**2 + i[3]**2]

xdist = np.concatenate(dist(*p) for p in (x, y))
ydist = np.concatenate(dist(*q) for q in (x, y))
