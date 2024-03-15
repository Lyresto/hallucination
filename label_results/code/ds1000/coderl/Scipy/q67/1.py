def column_zscore(df):
	print(df)
	x = [sum(1 for _ in df[row]) for row in df]
	y = sorted(df.index, key=lambda x: x.split("_")[1])
	z = [x[i] - x[i-1] for i in range(1, len(x))]
	print((z))
	return z
