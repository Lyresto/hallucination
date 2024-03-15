def f(dict=example_dict, df=example_df):
	for c, v in enumerate(df['Member']):
		df[c] = df[c].apply(lambda d: dict.get(d, d), axis=1)
	return df
