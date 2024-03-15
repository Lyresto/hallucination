import numpy as np
import scipy.spatial
distance.cdist = lambda y, x: scipy.spatial.distance.cdist(y,x).round(3)
