def plot_df(x, y):
	df = pd.DataFrame(y)
	for i in df:
		df.plot(x, i, color='r')
	plt.xlabel('X')
	# SOLUTION END
	return df
