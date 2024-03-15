from itertools import product

def heatmap(arr):
	xs, ys = list(zip(*arr))
	return plt.pcolormesh(xs, ys, cmap="Greys")
