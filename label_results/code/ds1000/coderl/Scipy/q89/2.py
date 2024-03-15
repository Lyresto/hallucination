class Solution:
	def transform(self):
		import copy
		weights = self.__WeightMatrix__
		for i in range(weights.shape[1]):
			weights[:,i] /= math.sqrt(sum(weights[:,i]))
		return copy.deepcopy(weights)
