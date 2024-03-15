
def bar_plot(df, y_vars):
	# Yum - X-Axis
	# Rotate 90 degrees
	x_ticklabels = [
		df['celltype'][i]
		for i in range(len(df['celltype']))
		if i % 2 == 0
	]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	bar_width = 0.35
	for i in range(len(y_vars)):
		ax.bar(
			x_ticklabels,
			df['s1'][i],
			bar_width,
			color='#444444',
		)
	ax.set_xticks(x_ticklabels)
	ax.set_xticklabels(x_ticklabels[::-1][:-1], rotation=45)
	return fig
