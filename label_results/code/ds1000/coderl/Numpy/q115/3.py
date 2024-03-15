from numpy import array
def find_maximum_index(a, index):
	return max(array(a)[indices == i] for i in range(len(a)))
