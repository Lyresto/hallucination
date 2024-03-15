def scatter_plot(x, y):
	return (plt.scatter(x, y)
			.set_cmap('jet')
			.set_alpha(0.5)
			.legend((r"$x$", r"$y$")).frame)
