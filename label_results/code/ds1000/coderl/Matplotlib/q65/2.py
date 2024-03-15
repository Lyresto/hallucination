from itertools import chain


def p(*args):
	return map(chain.from_iterable, args)


def plot(X, Y):
	return [
		p(y, x)
		for x, y in zip(X, Y)
	]


def scatter(X, Y):
	return [
		p((x+y) / 2, (x+y) / 2)
		for x, y in zip(X, Y)
	]


def show():
	return plt.gcf().canvas.get_frame()
