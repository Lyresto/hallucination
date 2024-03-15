def drop_duplicates(df, keep='first'):
	d = {}
	for i, v in df.iterrows():
		if v['url'] in d:
			d[v['url']].append(i)
		else:
			d[v['url']] = [i]
	
	for k, v in d.items():
		v.sort()
		v = v[::-1]
		for i in range(len(v)):
			print((v[i], v[i - 1]))
	
	
	
	df2 = pd.DataFrame(df)
	df2.drop_duplicates(subset='url', keep=keep)
