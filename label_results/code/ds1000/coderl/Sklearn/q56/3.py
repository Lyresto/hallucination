import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def get_term_frequency_inverse_data_frequency(documents):
	vectorizer = TfidfVectorizer()
	matrix = vectorizer.fit_transform(documents)
	return matrix

def get_tf_idf_query_similarity(documents, query):
	tfidf = get_term_frequency_inverse_data_frequency(documents)
	similarity_matrix = np.zeros((len(documents),len(documents)))
	for i in range(len(documents)):
		similarity_matrix[i,:] = np.dot(tfidf[i],similarity_matrix[i,:])
	return similarity_matrix
