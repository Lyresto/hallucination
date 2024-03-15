# Transform the query using the tfidf vectorizer
query_tfidf = tfidf.transform(queries)

# Compute the cosine similarities between the query and documents
cosine_similarities = np.dot(query_tfidf, tfidf_matrix.T).toarray()

# Create a dataframe to store the results
df = pd.DataFrame(cosine_similarities, columns=documents)

# Print the resulting dataframe
print(df)
