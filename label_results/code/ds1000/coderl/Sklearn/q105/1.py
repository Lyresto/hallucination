def train_test_split(df, train_size=0.8):
	df = df.sort(["date"])
	n = len(df)
	x = n * train_size
	y = (n-1)*train_size
	return df[:x], df[y:]
