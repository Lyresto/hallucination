def scatter(a, b, c):
	x, y = zip(*sorted(zip(a, b)))
	return (plt.scatter(x, y, c=c))

# make stacked bar plot
d = {i: [] for i in c}
for i, j in zip(c, c[1:]):
	d[i].append(j)
d = pd.concat(d.values())
d.plot.bar(x='b', y='a', width=0.5)
