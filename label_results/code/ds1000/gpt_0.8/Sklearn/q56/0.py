# Transform the query into a tf-idf vector representation
query_vector = tfidf.transform(queries)

# Calculate the cosine similarity between the query vector and the document vectors
cosine_similarities_of_queries = np.dot(query_vector, tfidf_matrix.T)

# Convert the cosine similarities into a dataframe for easier visualization
cosine_similarities_of_queries = pd.DataFrame(cosine_similarities_of_queries, columns=documents)
