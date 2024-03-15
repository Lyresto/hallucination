from sklearn.cluster import AgglomerativeClustering

# Convert the distance matrix to a condensed form
dist_condensed = squareform(simM)

# Perform hierarchical clustering
clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
cluster_labels = clustering.fit_predict(dist_condensed)

# Convert the cluster labels to a list
cluster_labels = cluster_labels.tolist()
