# First, calculate the centroid of each cluster
cluster_centroids = np.zeros((centroids.shape[0], data.shape[1]))
for i, centroid in enumerate(centroids):
    cluster_data = data[result == i] # extract data points in cluster i
    cluster_centroids[i] = np.mean(cluster_data, axis=0) # calculate centroid of cluster i

# Next, find the closest point to each cluster centroid
closest_points = np.zeros((centroids.shape[0], data.shape[1]))
for i, centroid in enumerate(cluster_centroids):
    cluster_data = data[result == i] # extract data points in cluster i
    closest_point = cluster_data[scipy.spatial.distance.cdist([centroid], cluster_data).argmin()] # find closest point to centroid
    closest_points[i] = closest_point

result = closest_points