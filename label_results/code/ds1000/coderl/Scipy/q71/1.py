def get_distance_2(y, x):
	mid =...  # needs to be a array of the shape (rows, cols, 2)?
	return scipy.spatial.distance.cdist(scipy.dstack((y, x)), mid)
