def plot_xy(x, y):
	return (pd.Series(y, index=x)).plot(kind='bar', x='X')


fig = plot_xy(x, y)

# Make both the x and y axis labels red
ax = fig.gca()
ax.set_xscale('linear')
ax.set_yscale('linear')
