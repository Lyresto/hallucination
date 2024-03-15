from itertools import cycle

def plot_two_subplots(x, y):
	# make x-axes
	xs = cycle(range(x))
	ys = cycle(y)
	xs = list(xs)
	# make y-axes
	ys = list(ys)
	fig, axs = [], []
	for ax, y in zip(axs, ys):
		ax.plot(y, x, 'b-')
	for ax, x in zip(axs, xs):
		ax.plot(x, y, 'r-')
	for ax, x in zip(axs, xs):
		ax.set_title('Y')
	# make 2-grid
	xs = np.arange(0, x.size)
	ys = [next(ys) for _ in range(xs.size)]
	for ax, y in zip(axs, ys):
		ax.plot(y, x, 'g-')
	for ax, x in zip(axs, xs):
		ax.plot(x, y, 'b-')
	for ax, x in zip(axs, xs):
		ax.set_title('X')
	# make 3-grid
	x = pd.Series(x)
	ys = [next(ys) for _ in range(x.size)]
	for ax, y in zip(axs, ys):
		ax.plot(y, x, 'g-')
	for ax, x in zip(axs, xs):
		ax.plot(x, y, 'b-')
	for ax, x in zip(axs, xs):
		ax.set_title('Y')
	# SOLUTION END
	return fig
