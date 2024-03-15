def dfs(df, start_year, end_year):
	print(end_year)
	for i in range(start_year, end_year + 1):
		df.ix[i, 'CumAve'] = sum(df.ix[i, 'Name'])/len(df.ix[i, 'Name'])
	for i in range(start_year, end_year + 1):
		if df.ix[i, 'CumAve']!= 0:
			df.ix[i, 'CumAve'] = df.ix[i, 'CumAve'] / float(len(df.ix[i, 'CumAve']))
