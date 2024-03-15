from scipy.sparse import csr_matrix
import numpy as np
import pandas as pd

def select_features(X,y):
	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(X)
	df = pd.DataFrame(X)
	X_scores = vectorizer.inverse_transform(X).T
	scores = []
	for i in range(len(X_scores)):
		if X_scores[i] > 0:
			scores.append(i)
	return scores
