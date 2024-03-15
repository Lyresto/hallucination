def f(df=example_df):
	# your code
	s = 0
	for i in df.values:
		s += i
	return s/len(df)
