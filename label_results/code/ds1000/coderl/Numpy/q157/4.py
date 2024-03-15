import numpy as np
x_dists = np.array([[ 0, -1, -2],
                 [ 1,  0, -1],
                 [ 2,  1,  0]])
y_dists = np.array([[ 0, 1, -2],
                 [ -1,  0, 1],
                 [ -2,  1,  0]])

dist = np.concatenate((x_dists, y_dists), axis = 0)

def dist_between_two_points(x, y):
	return list(itertools.accumulate(np.abs(x_dists - np.expand_dims(x, 1)).reshape(3, 2), axis = 0))
