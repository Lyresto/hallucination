def distances(patch):
	return scipy.spatial.distance.pdist(patch).round(decimals=1).tolist()
