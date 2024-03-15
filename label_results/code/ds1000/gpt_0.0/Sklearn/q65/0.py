# Convert the similarity matrix to a distance matrix
distM = 1 - np.array(simM)

# Perform hierarchical clustering using complete linkage
agg_clustering = sklearn.cluster.AgglomerativeClustering(n_clusters=2, linkage='complete', affinity='precomputed')
cluster_labels = agg_clustering.fit_predict(distM)

# Print the cluster labels
print(cluster_labels)
