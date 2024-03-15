import math

class SparseMatrix:
	def __init__(self, weight_matrix):
		self.__weight_matrix = weight_matrix
		self.shape = weight_matrix.shape
	
	@property
	def data(self):
		return self.__weight_matrix.data

	@data.setter
	def data(self, value):
		self.__weight_matrix.data = value
