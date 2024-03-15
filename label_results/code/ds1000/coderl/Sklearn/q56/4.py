import numpy as np
import pandas as pd
def get_term_frequency_inverse_data_frequency(documents):
	vectorizer = TfidfVectorizer()
	matrix = vectorizer.fit_transform(documents)
	return matrix

def get_tf_idf_query_similarity(documents, query):
	tfidf = get_term_frequency_inverse_data_frequency(documents)
	query_matrix = tfidf.transform([query])
	return query_matrix[:, 1:]

def cosine_similarities_of_queries(queries, documents):
	cosine_similarities = []
	for query in queries:
		query_matrix = get_tf_idf_query_similarity(documents, query)
		similarities = np.dot(query_matrix, query_matrix)
		cosine_similarities.append(similarities)
	return np.array(cosine_similarities).T
