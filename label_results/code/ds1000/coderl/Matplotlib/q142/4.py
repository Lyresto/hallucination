def plot_one(x, y):
	d = pd.Series(y)
	ax = d.plot(x, y, color='blue', alpha=.5)
	return ax

def plot_two(x, y):
	d = pd.Series(y)
	ax1 = d.plot(x, 'k', color='g', alpha=.5)
	return ax1

def plot_three(x, y):
	d = pd.Series(x)
	ax2 = d.plot(x, 'r', alpha=.5)
	return ax2

def plot_four(x, y):
	d = pd.Series(x)
	ax3 = d.plot(x, 'b', alpha=.5)
	return ax3
