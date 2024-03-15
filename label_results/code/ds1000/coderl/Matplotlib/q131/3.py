from itertools import cycle, chain

def make_xy(n):
	return list(zip(cycle(range(n)), cycle(range(n))))

def scatter(x, y, *args):
	return sum(map(lambda a, b: a[0].plot(b, *args), zip(x, y)))

def plot(*args, **kwargs):
	return sum(map(scatter, *args, **kwargs), **kwargs)

def line(*args, **kwargs):
	return sum(map(line, args, kwargs), **kwargs)

def grid(n, *args, **kwargs):
	return [line(*args, **kwargs) for _ in range(n)]

def _p(*args, **kwargs):
	return plot(*args, **kwargs).get_figure()
