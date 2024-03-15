def line_plot(df, x=0, y=1):
	df.plot.line(x, y, linewidth=2, diamond=True)
	return df.plot.get_figure()
