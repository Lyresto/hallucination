import numpy as np
from scipy.spatial import cosine_similarity

def get_tf_idf_query_similarity(queries, documents):
	vectorizer = TfidfVectorizer()
	matrix = vectorizer.fit_transform(documents)
	return cosine_similarity(matrix, queries).tolist()

def get_term_frequency_inverse_data_frequency(documents):
	vectorizer = TfidfVectorizer()
	matrix = vectorizer.fit_transform(documents)
	return matrix.toarray()
