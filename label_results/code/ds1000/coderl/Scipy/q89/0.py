import numpy as np

class WeightMatrix:

	def __init__(self, weight_matrix):
		weight_matrix = np.array(weight_matrix)
		self.__WeightMatrix__ = weight_matrix
		self.shape = weight_matrix.shape

	def __mul__(self, other):
		if type(other)!= WeightMatrix:
			return NotImplemented
		weight_matrix = self.__WeightMatrix__
		for i in range(self.shape[1]):
			other.__WeightMatrix__[:,i] = (weight_matrix[:,i] * other.__WeightMatrix__[:,i]).normalize()
		return other
