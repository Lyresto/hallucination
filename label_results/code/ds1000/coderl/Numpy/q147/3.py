import numpy as np
def pearson(post, distance):
	print(post, distance)
	count_p = np.array(post).count()
	count_d = np.array(distance).count()
	if count_p == 0 or count_d == 0:
		return 0
	return (count_p - count_d) / (count_p - count_d)
