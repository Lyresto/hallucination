import numpy as np
from scipy.spatial import distance

def get_distance_2(y, x):
    mid = np.array([[shape[0]//2, shape[1]//2]])
    points = np.column_stack((y.flatten(), x.flatten()))
    distances = distance.cdist(points, mid, 'euclidean')
    return distances.reshape(shape)

y, x = np.indices(shape)
result = get_distance_2(y, x)
result