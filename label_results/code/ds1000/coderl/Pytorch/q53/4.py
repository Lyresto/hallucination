from collections import Counter

def cnt_not_equal(a, b):
	return sum(v1!=v2 for v1,v2 in zip(a,b))
