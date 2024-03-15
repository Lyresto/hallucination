import numpy as np

def pos_of_smallest(a):
	return [i[0] for i in enumerate(a) if np.min(a).tolist() == a].index(min(a))
