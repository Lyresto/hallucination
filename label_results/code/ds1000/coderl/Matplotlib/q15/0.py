from itertools import zip_longest

df = pd.DataFrame(zip_longest(x, y), columns=['x', 'y'])
for p, (ax1, ax2) in enumerate(df.plot.values()):
	ax2.set_linewidth(7)
	ax1.set_markersize(2)
	p += 1
