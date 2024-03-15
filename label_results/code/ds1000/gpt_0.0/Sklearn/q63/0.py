# Convert distance matrix to condensed distance matrix
dist_matrix = np.sqrt(2*(1-np.array(data_matrix)))
condensed_dist_matrix = pdist(dist_matrix)

# Perform hierarchical clustering
agg_clustering = sklearn.cluster.AgglomerativeClustering(n_clusters=2, linkage='average', affinity='precomputed')
agg_clustering.fit_predict(squareform(condensed_dist_matrix))

# Convert cluster labels to list
cluster_labels = agg_clustering.labels_.tolist()
