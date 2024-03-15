import numpy as np
import scipy.sparse as sp

def have_element(i, j):
	return i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	
def make_symmetric():
	lil = sp.lil_matrix(M)
	for i in range(lil.shape[0]):
		for j in range(lil.shape[1]):
			if i!= j:
				lil[i, j] = lil[j, i]
	lil.make_symmetric()
	return lil
