def zscore(df):
	res = []
	for i, c in enumerate(df.index):
		x = df.loc[c]
		res.append((len(df.index)-i-1, x))
	res.sort()
	sm, p = 0, 0
	for i, r in enumerate(res):
		sm += r[0]
		p += r[1]
	return sm, p
def column_zscore(df):
	sm, p = zscore(df)
	return (sm, p)
