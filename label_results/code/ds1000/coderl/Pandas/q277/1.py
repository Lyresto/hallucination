def sort_data(df):
	t, d, t1, d1 = df.index.levels[0], df.index.levels[1], df.index.levels[2], df.index.levels[3]
	vims = sorted(df['VIM'], key=lambda x: (x, t1, d1))
	df['VIM'] = vims
	df = df.sort_values(by=t, by_row=d1, by_col=t1)
	return df
