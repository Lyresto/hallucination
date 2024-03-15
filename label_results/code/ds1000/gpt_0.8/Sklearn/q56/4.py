# Transform the query into tf-idf representation
query_tfidf = tfidf.transform(queries)

# Calculate the cosine similarities between the query and the documents
cosine_similarities = np.dot(query_tfidf, tfidf_matrix.T)

# Normalize the similarities between 0 and 1
normalized_cosine_similarities = (cosine_similarities + 1) / 2

# Convert the similarities into a dataframe
df_similarities = pd.DataFrame(normalized_cosine_similarities, columns=documents)

# Print the dataframe
df_similarities
