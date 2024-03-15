import scipy.cluster.hierarchy
from scipy.spatial import ConvexHull

def closest_to_centroid(centroids, data):
	linkage = scipy.cluster.hierarchy.linkage(data, metric='cosine')
	clusters = [convex_hull(point) for point in linkage]
	return [i for i, cluster in enumerate(clusters) if i == min(result)][0]
