def plot_heatmap(data):
	f, (a1, a2), (b1, b2) = plt.subplots(4, 5, sharex=True, sharey=True)
	for x, y in data:
		f.text(x, y, f'{x}{y}', color='#A01228E')
	f.set_size_inches(4, 4)
	return f
