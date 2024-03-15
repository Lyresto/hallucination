from itertools import cycle

def plot_x_y(x, y):
	cs = cycle([(x, y), (x[1:], y[1:])])
	for _ in range(10):
		fig, ax = next(cs)
		ax.plot(*zip(*ax))

def plot_y_x(x, y):
	cs = cycle([(x, y), (x[1:], y[1:])])
	for _ in range(10):
		fig, ax = next(cs)
		ax.plot(*zip(*ax))

def plot_xy(x, y):
	plt.plot(x, y, 'ro')

def plot_xy_diag(x, y):
	xy = np.array([x, y]).T
	xy_diag = pd.DataFrame(xy, index=x)
	xy_diag.plot(ax=None, x_k=0, y_k=1, kind='barh')
	return xy_diag.plot(ax=None, x_k=0, y_k=1, kind='lines')
