import tensorflow as tf

def mask_tensor(t):
	n = 8
	return [ [0]*8 for _ in range(n) ] + [ [1]*8 for _ in range(n) ]
