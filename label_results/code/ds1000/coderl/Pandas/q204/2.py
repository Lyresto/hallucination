def f(df=example_df):
	# your code here
	result = []
	for i in range(len(df['Name'])):
		result.append(sum(df['200%s' % i])/len(df['200%s' % i]))
	return pd.Series(result)
