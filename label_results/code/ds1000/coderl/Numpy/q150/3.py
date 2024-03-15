import numpy as np

def is_contained(a):
	number = 0
	for x in a:
		if x == number:
			return True
		else:
			number += 1
	return False
