query_tfidf = tfidf.transform(queries)
cosine_similarities_of_queries = np.dot(query_tfidf, tfidf.T).toarray()
