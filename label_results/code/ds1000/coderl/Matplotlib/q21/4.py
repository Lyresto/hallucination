import math
from itertools import cycle, zip_longest

def rotate(xys):
	return [(int(math.atan(d) + (2*np.pi/30)), d) for d in xys]

def scatter(xys):
	xs, ys = zip_longest(*xys)
	ax = sns.jointplot(*xs, y=ys, color="#555555")
	return ax.get_figure()

def kde(xys):
	kds = [np.sin(x) for x in xys]
	return kds, kds[0]

def plot_stacked_kde(df):
	kds, kde_xys = kde(df)
	for k, v in kds:
		ax = k.plot(kde_xys, label=f"{k}")
	ax.set_xlabel("k")
	ax.set_ylabel("cos(k)")

# SOLUTION END
