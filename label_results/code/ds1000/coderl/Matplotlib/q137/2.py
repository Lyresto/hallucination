def make_subplots(num, *args):
	if isinstance(args[0], (list, tuple, np.ndarray)):
		return [make_subplots(*args[0])]
	else:
		return make_subplots(*args)

def print_subplots(num, *args):
	for i, plot in enumerate(make_subplots(args[0], *args[1:])):
		print(plot.xaxis.get_label(), end="")
	print("")

def axis_label(num):
	for i, plot in enumerate(make_subplots(num, *args)):
		if len(plot.xaxis.get_label()) > 0:
			return plot.xaxis.get_label()[0]
		return "x"

def plot_line(a, b):
	return plt.plot(a, b, "r-", label="line")

def scatter_line(a, b):
	return plt.plot(a, b, "b-", label="scatter")

def diag(a, b):
	return plt.plot(a, b, "g-", label="diag")

def twinx(a, b):
	return plt.twinx(a, b)

def trwinx(a, b):
	return plt.trwinx(a, b)

def plot_both(a, b):
	return plot_line(a, b)
	return plot_line(b, a)

def plot_diag(a, b):
	return plot_diag_line(a, b)
	return plot_diag_line(b, a)

def plot_line_diag(a, b):
	return plot_line(a, b, "l-", label="line diag")

def plot_diag_line(a, b, l):
	return plot_diag(a, b, "r-", l)

def get_test_data():
	a = np.arange(10).reshape(2, 5)
	b = np.arange(10).reshape(2, 5)
	return a