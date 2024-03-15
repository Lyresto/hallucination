# def test_remove_contour(c):
#     print(c in CNTS)
#     print(c in CNTS[0])
#     return True

# def test_remove_contour(c):
#     print(c in CNTS)
#     print(c in CNTS[0])
#     return True

import numpy as np

def test_is_contour_member(c, CNTS):
	print(c in CNTS)
	print(c in CNTS[0])
	return np.all(c in CNTS)
