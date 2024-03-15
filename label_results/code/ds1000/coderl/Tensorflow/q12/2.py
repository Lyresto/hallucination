import numpy as np

def f(lengths=example_lengths):
	return np.pad(np.array(lengths), mode="constant", constant_value=0)
