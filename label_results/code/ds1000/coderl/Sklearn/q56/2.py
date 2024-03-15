def cosine_similarities_of_queries(queries, documents):
	vectors = get_term_frequency_inverse_data_frequency(documents)
	cosine_similarities_of_queries = []
	for query in queries:
		similarities = []
		for document in documents:
			if query in document:
				similarities.append(document.count(query) * 1.0 / (len(document) - document.count(query)))
		cosine_similarities_of_queries.append(similarities)
	return pd.DataFrame(cosine_similarities_of_queries, index=queries)
