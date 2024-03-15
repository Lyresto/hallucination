import scipy.spatial as sp
from itertools import combinations

def distance(example_array, example_ids):
	return min(
		[sp.distance.cdist(example_array[i], example_array[j])
		 for i in range(len(example_array))
		 for j in range(len(example_array))]
	)

def plot_distances(distances):
	from itertools import product
	from collections import Counter
	from itertools import product
	from operator import mul
	print(distances)
	for i in product(range(len(distances)), repeat=len(distances)):
		print(*(map(str, i)), sep=' ')
