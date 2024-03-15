from itertools import product

def select_features(corpus, y):
	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(corpus)
	p = list(product(list(range(len(corpus))), repeat=2))
	res = [name for name,score in p if score in X[i]]
	return res
