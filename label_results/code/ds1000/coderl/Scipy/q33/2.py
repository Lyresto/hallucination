import scipy.ndimage
def prune_noise(square):
	return scipy.ndimage.maximum_filter(square, size=(1,1), mode="constant")
