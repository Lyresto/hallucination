from operator import itemgetter

def dfs_concat(df1, df2):
	city, district = (df1[c].values for c in 'city district'.split())
	return pd.merge(df1, df2, on='id')[
		[k for k, v in zip(city.take(n=len(city)), district.take(n=len(district))),
		 'value']].copy()
