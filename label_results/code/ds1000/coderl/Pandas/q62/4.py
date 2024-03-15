def replace_each_a(df):
	df["a"] = df["a"].apply(lambda x: str(x + 1))
	return df
