def is_contour_member(c, Contours):
	return all(all(isinstance(x, list) and len(x) == len(Contours) and len(set(x)) == len(Contours) for x in x)) and c in Contours
