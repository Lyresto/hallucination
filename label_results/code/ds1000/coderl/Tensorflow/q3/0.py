import numpy as np
from tensorflow.python.keras.metrics import accuracy

def accuracy(labels, predictions):
	return np.array(predictions).mean()
