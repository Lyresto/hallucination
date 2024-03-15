def is_contained(a):
	return sum(1 for x in a if x == x) == len(a)
