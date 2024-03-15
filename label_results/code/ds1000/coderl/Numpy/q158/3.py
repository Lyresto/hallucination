import numpy as np

def dist_between(x,y):
	[dist_x, dist_y] = x+y
	[min_dist_x, min_dist_y] = np.min(dist_x, dist_y)
	return [min_dist_x, min_dist_y, dist_x-dist_y]
	
def dist_from_xy(x,y):
	x_dist = [(dist_between(x,y)[0], x,y)]
	y_dist = [(dist_between(x,y)[1], x,y)]
	return x_dist + y_dist
	
def sort_xy(xys, new_xys):
	for x, (old, new) in enumerate(xys):
		xys[x] = new
	return xys
