def drop_duplicates(df, keep='first'):
	d = {}
	for i, v in df.iterrows():
		if v in d:
			d[v].append(i)
		else:
			d[v] = [i]
	print(d)
	for v in d:
		print(v, d[v][0], sep=' ')
