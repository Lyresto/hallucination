import numpy as np
from scipy import sparse

def yelpfilter(a):
	try:
		a = sparse.csr_matrix(a)
		return a
	except ValueError:
		return np.array(a)
