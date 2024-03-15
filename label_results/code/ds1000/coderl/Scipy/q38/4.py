def dist(A):
	return scipy.spatial.distance.pdist(A)

def plot_dist(A, x, y):
	return plt.plot(dist(A[:,x]), dist(A[:,y]), 'b-')
