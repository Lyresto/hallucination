from sklearn.cluster import AgglomerativeClustering

# Create a distance matrix
distance_matrix = np.array([[0, 0.8, 0.9], [0.8, 0, 0.2], [0.9, 0.2, 0]])

# Perform hierarchical clustering
model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
cluster_labels = model.fit_predict(distance_matrix)

cluster_labels