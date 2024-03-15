def fillna(df, n=0.5):
	for c in df:
		if c!=0:
			df[c] = (df[c] + (n/100)*1.0).round(n)
			n += 1
