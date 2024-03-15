from itertools import zip_longest

def plot_series(s):
	xs, ys = zip_longest(s, s, fillvalue=0)
	return [plot(xs, y) for y in ys]

def plot(xs, ys):
	return plt.plot(xs, ys, 'o')
