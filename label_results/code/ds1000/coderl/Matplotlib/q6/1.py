def plot_line(df, x, y, color):
	ax = df.plot(x=x, y=y, color=color)
	return ax

def random_plot(df):
	df['X'] = np.random.randint(0, 10)
	df['Y'] = np.random.randn()
	return plot_line(df, *df.columns.values, color='g')

def square_plot(df):
	df['X'] = np.linspace(0, 10, 10)
	df['Y'] = np.zeros_like(df.X) + np.random.randn(10)
	return plot_line(df, *df.columns.values, color='b')
