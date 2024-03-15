import numpy as np
import pandas as pd

def get_mask(lens):
	# return the solution in this function
	lens = [len(s) for s in lens]
	num_of_words = sum(lens)
	mask = np.ones(num_of_words, dtype=np.int64) * 2 - 1
	return mask.tolist()
