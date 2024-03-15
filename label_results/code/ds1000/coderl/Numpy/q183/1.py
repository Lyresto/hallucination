def remove_contour(c, contours):
	print(c in contours)
	for i,contour in enumerate(contours):
		if np.all(np.isnan(contour)):
			contours.remove(contour)
			break
	return len(contours)==0
