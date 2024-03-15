import numpy as np
def slicing(Z):
	# your code
	try:
		return Z[-1:]
	except:
		return Z[:-1]
