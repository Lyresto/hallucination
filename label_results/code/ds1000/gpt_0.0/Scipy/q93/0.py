result = []
for i in range(len(centroids)):
    cluster_points = data[np.where(labels == i)[0]]
    distances = scipy.spatial.distance.cdist(cluster_points, [centroids[i]])
    closest_point_idx = np.argmin(distances)
    closest_point = cluster_points[closest_point_idx]
    result.append(closest_point)
