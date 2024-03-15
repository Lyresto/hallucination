from sklearn.cluster import AgglomerativeClustering

# Create the hierarchical clustering model
model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')

# Perform clustering on the distance matrix
cluster_labels = model.fit_predict(data_matrix)

END SOLUTION
