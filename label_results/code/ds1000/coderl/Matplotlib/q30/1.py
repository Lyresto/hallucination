from itertools import zip_longest

def plot(x, y):
	xs, ys = zip_longest(x, y)
	return [(i, j) for i, j in zip_longest(xs, ys, fillvalue=0)]

def mean(x):
	return sum(x)/len(x)

def plot2d(x, y, z):
	return [plot(x, z) for _ in range(y)]

df = pd.DataFrame({"x": x, "y": y})
df["z"] = mean(df["x"])
df["y"] = mean(df["y"])


# plot2d(df["x"], df["y"], df["z"])

# SOLUTION END
