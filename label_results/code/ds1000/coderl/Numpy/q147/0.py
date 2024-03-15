import numpy as np
def correlation(post, distance):
	post = np.array(post)
	distance = np.array(distance)
	return np.sum(np.array(post).reshape(-1, 1) * np.array(distance).reshape(-1, 1)) / (np.array(post).sum() - np.array(distance).sum())
