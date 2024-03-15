from math import ceil, log

def f(x):
	return ceil((x * 2 - log(x)) / log(2))

def plot(x, y):
	p = (x * 2 - log(x)) / log(2)
	return p.plot(y, x)

# solving the kata
d = pd.DataFrame({"x": x, "y": y})
a = plot(d["x"], d["y"])
