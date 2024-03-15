import numpy as np
import scipy.ndimage

def reduce_noise(square):
	return np.zeros_like(square) * np.minimum(square.shape) + square
