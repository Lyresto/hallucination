from sklearn.cluster import AgglomerativeClustering

# Creating the AgglomerativeClustering object
clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')

# Fitting the data matrix
clustering.fit(data_matrix)

# Getting the cluster labels
cluster_labels = clustering.labels_

# Printing the cluster labels
print(cluster_labels)
