from copy import deepcopy
from scipy.spatial import ConvexHull
def Transform(a):
	return deepcopy(a).map(lambda x: ConvexHull(a).transform(a).tolist()[0])
