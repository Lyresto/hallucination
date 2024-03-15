def f(a=example_a):
	# import numpy as np
	# from scipy.stats import rankdata
	
	# a = np.array(a)
	# result = rankdata(a).astype(int)
	# x = np.sort(result,reverse = True)
	
	# print(x)
	
	
	
	from numpy import argsort
	a = np.array(a)
	result = argsort(a, kind='mergesort')
	print(result)
	return result[:,-1]
	
