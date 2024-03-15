def zscore(df, x):
	# your code
	zscore = lambda x: sum(df[x].values())/len(df[x])
	return [zscore(i) for i,row in df.iterrows()]


