import numpy as np

def is_contained(a):
	if len(a) == 0:
		return False
	elif len(a) == 1:
		if a[0] == 0:
			return False
		else:
			return True
	else:
		for n in range(len(a)):
			if a[n] == 0:
				return False
			elif n > 1:
				if a[n - 1] == 0:
					return False
		return True
