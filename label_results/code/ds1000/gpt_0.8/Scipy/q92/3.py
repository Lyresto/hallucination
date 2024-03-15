dist_matrix = scipy.spatial.distance.cdist(data, centroids)
cluster_assignments = scipy.cluster.hierarchy.cut_tree(linkage_matrix, n_clusters=5).flatten()

result = []
for i in range(5):
    cluster_indices = np.where(cluster_assignments == i)[0]
    cluster_distances = dist_matrix[cluster_indices, i]
    closest_index = cluster_indices[np.argmin(cluster_distances)]
    result.append(closest_index)
result = np.array(result)