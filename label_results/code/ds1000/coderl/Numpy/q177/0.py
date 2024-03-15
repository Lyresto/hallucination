from numpy import array, window

def sliding_window(a, size, center=None):
	if center is None:
		center = (size[0]//2, size[1]//2)
	return [array(window(a[i*size[0]:(i+1)*size[0], center=center, axis=i))
			for i in range(size[0])]
