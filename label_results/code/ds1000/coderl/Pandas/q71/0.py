def f(df, columns=['b', 'e']):
	return sum(df[c].sum() for c in columns if df[c].max() > 0.5)
