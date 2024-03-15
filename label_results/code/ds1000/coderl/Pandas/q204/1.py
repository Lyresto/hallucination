def f(df=example_df):
	s = 0
	for i in df.itertuples():
		s += i[1]
	return round(s / len(df.values))
