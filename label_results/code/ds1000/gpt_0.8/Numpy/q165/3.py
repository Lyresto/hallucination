import numpy as np
from scipy.spatial.distance import pdist, squareform

a = np.array([[1,2,8],
     [7,4,2],
     [9,1,7],
     [0,1,5],
     [6,4,3]])

distances = pdist(a)
result = squareform(distances)

print(result)
