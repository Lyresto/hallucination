import numpy as np

class csr_matrix:
	def __init__(self, Feature):
		try:
			self.data = np.concatenate(Feature)
		except:
			self.data = np.array(Feature)
		self.shape = (len(Feature), len(Feature[0]))

	def __getitem__(self, Index):
		try:
			return self.data[Index]
		except:
			return self.data[:, Index]

	def __len__(self):
		return self.data.shape[0]

	def __str__(self):
		return str(self.data)
