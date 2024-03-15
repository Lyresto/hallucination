query_vectors = tfidf.transform(queries)
document_vectors = tfidf.transform(documents)
cosine_similarities_of_queries = np.dot(query_vectors, document_vectors.T).toarray()
