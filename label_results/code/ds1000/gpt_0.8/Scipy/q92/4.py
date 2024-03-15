import numpy as np
import scipy.spatial

def get_closest_element(centroids, data):
    closest_elements = []
    for centroid in centroids:
        distances = scipy.spatial.distance.cdist([centroid], data)
        closest_index = np.argmin(distances)
        closest_elements.append(closest_index)
    return closest_elements

result = get_closest_element(centroids, data)
