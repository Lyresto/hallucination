class SparseMatrix:

	def __init__(self, weight_matrix):
		self.__WeightMatrix__ = weight_matrix.tocsr()
		self.shape = weight_matrix.shape[1]

	def dot(self, scalar_product, matrix):
		for i in range(self.shape[1]):
			matrix[i,i] = scalar_product * matrix[i,i]
		return matrix
