import numpy as np
from scipy.spatial import distance

def get_distance_2(y, x):
	mid = np.array([[y[i][j], x[i][j]], [y[i][0], x[i][0]], [y[i][j], x[i][j]], [y[i][0], x[i][0]], [y[i][j], x[i][j]]])
	return distance.cdist(mid).tolist()
