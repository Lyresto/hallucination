def test_contour_is_member_of_contour_list(c, contours):
	print(c in contours)
	print((c in contours), type(c))
	print((c in [c[0]]), type(c[0]))
