import numpy as np

def pearson_coefficient(post, distance):
	return np.linalg.det(np.array(post) - np.array(distance)) / np.linalg.det(np.array(distance))
