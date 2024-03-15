class Pipeline:

	def __init__(self, estimators):
		self.estimators = estimators

	def named_steps(self):
		return {name: self.steps[name] for name in self.steps}

	def __setitem__(self, key, value):
		if key not in self.steps:
			raise ValueError
		self.steps[key] = value

	def __getitem__(self, key):
		return self.steps[key]
