import scipy.sparse

class SparseMatrix(object):
	"""
	A sparse matrix is a way to construct another sparse matrix.
	This is equivalent to adding the two sparse matrices horizontally,
	horizontally and vertically.
	"""
	def __init__(self, Feature):
		try:
			self.s = scipy.sparse.csr_matrix(Feature)
		except:
			raise ValueError("Feature must be a list or csr_matrix.")
	def __getitem__(self, index):
		try:
			return self.s.row[index]
		except:
			return self.s.col[index]

	def __setitem__(self, index, value):
		try:
			self.s.row[index] = value
			self.s.col[index] = value
		except:
			raise ValueError("Index must be a slice or an integer.")
