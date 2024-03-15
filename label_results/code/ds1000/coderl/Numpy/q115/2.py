import numpy as np
def max_of_elements_in_index(a,index):
	return np.array([max(a[i] for i in index)])
