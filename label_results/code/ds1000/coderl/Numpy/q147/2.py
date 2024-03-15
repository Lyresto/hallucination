import numpy as np
def pearson(post,distance):
	post = np.array(post)
	distance = np.array(distance)
	return np.linalg.norm(post-distance)**2
