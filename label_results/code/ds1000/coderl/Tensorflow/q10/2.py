import tensorflow as tf

def mask_tensor(lengths):
	len_array = 8
	len_mask = 8
	len_mask_matrix = [[0]*len_mask for _ in range(len_array)]
	for i in range(len_array):
		len_mask_matrix[i][i] = (1-int(lengths[i]))%2
		len_mask_matrix[i][i+1] = (1-int(lengths[i+1]))%2
	return len_mask_matrix
