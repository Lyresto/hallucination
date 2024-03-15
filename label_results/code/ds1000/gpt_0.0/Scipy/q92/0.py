result = []
for i in range(len(centroids)):
    cluster_indices = np.where(cut_tree == i)[0]
    distances = scipy.spatial.distance.cdist([centroids[i]], data[cluster_indices])
    closest_index = cluster_indices[np.argmin(distances)]
    result.append(closest_index)
