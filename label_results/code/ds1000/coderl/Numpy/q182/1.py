import numpy as np

def test_is_member_of_a_list_of_numpy_arrays(c, CNTS):
	print(c in CNTS)
	print(c in CNTS[0])
	print(c in CNTS[1:])
	return (c in CNTS).all()
