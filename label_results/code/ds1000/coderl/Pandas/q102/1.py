def f(df=example_df):
	for i, col in df.iterrows():
		df[i] = [val.replace('&', '&amp;') for val in col]
	return df
