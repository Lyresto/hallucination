import numpy as np
import tensorflow as tf

def accuracy(labels, result):
	return np.array(result).sum() / np.array(labels).sum()
