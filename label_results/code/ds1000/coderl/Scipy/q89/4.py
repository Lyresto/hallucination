import math

class SparseMatrix(object):
	def __init__(self, A):
		n = len(A)
		self.__WeightMatrix__ = [[0 for i in range(n)] for j in range(n)]
		for i, x in enumerate(A):
			self.__WeightMatrix__[i][0] = x[0]
			for j, y in enumerate(x[1:], start=1):
				self.__WeightMatrix__[i][j] = math.sqrt(sum(y**2))
		return
