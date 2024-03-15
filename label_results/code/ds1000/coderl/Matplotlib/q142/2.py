def plot_line_chart(x, y):
	df = pd.DataFrame({"x": x, "y": y})
	return plt.plot(df["x"], df["y"], "b")
