def f(df=example_df):
	total = 0
	for i, r in enumerate(df.values):
		total += r
	return total / len(df)
