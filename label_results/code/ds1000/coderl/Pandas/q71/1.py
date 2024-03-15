def f(df, columns=['b', 'e']):
	# df2 = df[df.c>0.5]
	df2 = df[columns]
	for col in columns:
		df2[col] = df2[col] + df2[col+1]
	return df2.sum(axis=1)
