import numpy as np
from scipy.spatial import distance

def get_distance_2(y, x):
    mid = np.array([[shape[1]/2, shape[0]/2]]) # center point
    points = np.dstack((y, x))
    distances = distance.cdist(points, mid)
    return distances

y, x = np.indices(shape)
result = get_distance_2(y, x)
print(result)
END SOLUTION
