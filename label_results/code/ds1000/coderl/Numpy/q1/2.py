import numpy as np
def remove_nans(x):
	a=[]
	for i in x:
		if i!=np.nan:
			a.append(i)
	return a
