import numpy as np

#def deep_copy(arrays):
#    nps = []
#    for array in arrays:
#        nps.append(np.array(array, copy=True))
#    return nps

def deep_copy(arrays):
	nps = []
	for array in arrays:
		nps.append(np.array(array, copy=True))
	return nps
