from sklearn.cluster import AgglomerativeClustering

# Convert similarity matrix to distance matrix
distM = 1 - simM

# Perform hierarchical clustering
clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
clustering.fit(distM)

# Get cluster labels
cluster_labels = clustering.labels_

# Print cluster labels
print(cluster_labels)
