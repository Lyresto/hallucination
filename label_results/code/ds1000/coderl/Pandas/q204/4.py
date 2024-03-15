def f(df=example_df):
	res = 0
	for i in range(len(df['Name'])):
		res += (sum(df[df['Name'][i]])/len(df['Name'][i]))
	return res
