# Calculate the distance between each data point and each centroid
distances = scipy.spatial.distance.cdist(data, centroids)

# Find the index of the closest centroid for each data point
closest_centroid_indices = np.argmin(distances, axis=1)

# Find the index of the closest element in original data for each cluster
result = np.zeros(centroids.shape[0], dtype=int)
for i in range(centroids.shape[0]):
    cluster_indices = np.where(closest_centroid_indices == i)[0]
    cluster_distances = distances[cluster_indices, i]
    closest_index = cluster_indices[np.argmin(cluster_distances)]
    result[i] = closest_index
