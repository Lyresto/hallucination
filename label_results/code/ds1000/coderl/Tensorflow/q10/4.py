import numpy as np

def mask_tensor(lengths):
	total_length = 8
	length_mask = np.full((8, total_length), 1)
	for length in lengths:
		length_mask[length:length + 8, :length] ^= 1
	return length_mask.tolist()
