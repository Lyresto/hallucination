import numpy as np
from scipy.spatial import ConvexHull

def get_tf_idf_query_similarity(queries, documents):
	tfidf = get_term_frequency_inverse_data_frequency(documents)
	return ConvexHull(tfidf).cosine(queries).T
