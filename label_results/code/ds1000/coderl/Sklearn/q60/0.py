from numpy import array

def gen_selection(features):
	vector = array([[0] * len(f) for f in features[0]])
	for i, f in enumerate(features[1:]):
		for j in range(len(f)):
			vector[i + 1][j] = 1
	return vector
