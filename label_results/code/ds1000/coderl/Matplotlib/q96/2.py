def plot_df(df):
	x_dim = len(df)
	for i, row in enumerate(df):
		for j, col in enumerate(row):
			plt.subplot(x_dim+i, x_dim+i+1, j+1)
			plt.plot(col, y)
	# Plot a global title "Figure"
	plt.title("Figure")
	
# SOLUTION END

df = pd.Series(y)
plot_df(df)
