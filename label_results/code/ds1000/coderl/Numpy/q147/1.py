import numpy as np

def pearson(post, distance):
	post_range = np.array(post)
	dist_range = np.array(distance)
	post_sum = post_range.sum()
	dist_sum = dist_range.sum()
	return np.dot(post_sum - dist_sum, (post_range - dist_range).T) / (np.dot(post_sum, dist_range).T - post_sum)

def solution():
	return pearson(post, distance)
