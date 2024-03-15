def select_features(X,y):
	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(X)
	selector = SelectKBest(selector='kbest')
	selector.fit(X,y)
	result = vectorizer.get_support()
	result_indices = [i for i in range(X.shape[1]) if result[i]]
	return result_indices

class SelectKBest:
	def __init__(self, k):
		self.k = k
		self.selector = None
	
	def get_support(self):
		if self.selector is None:
			return []
		return self.selector.get_support()
	
	def fit(self, X, y):
		if self.selector is None:
			self.selector = SelectKBest(k=self.k).get_support()
			return self.selector
		return self.selector.fit(X,y).transform(X)
