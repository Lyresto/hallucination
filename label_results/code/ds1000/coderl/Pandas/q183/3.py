def f(dict=example_dict, df=example_df):
	dic = {}
	for i, v in enumerate(df['Member']):
		if v in dict:
			dic[v] = dict[v]
		else:
			dic[v] = v
	return df.assign(**dic)
