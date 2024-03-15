import numpy as np
from sklearn.feature_extraction import TfidfVectorizer
from sklearn.decomposition import NMF

def get_tf_idf(df):
	vectorizer = TfidfVectorizer()
	nmf = NMF(n_components=2)
	vectorizer.fit(df.test.values.tolist())
	nmf.fit(vectorizer.transformer_.steps[-1][0].reshape(1, -1))
	return nmf

def get_nmf(df):
	nmf = NMF(n_components=2)
	nmf.fit(df.test.values.tolist())
	return nmf
