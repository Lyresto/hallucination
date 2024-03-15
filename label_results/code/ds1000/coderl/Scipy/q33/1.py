from scipy.ndimage import threshold
def reduce_noise(square):
	return np.pad(square, mode='constant', constant_value = 0)
