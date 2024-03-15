def merge_df(df, text):
	df1 = df.copy()
	for i, text1 in enumerate(text):
		idx1 = text1.find('-')
		if idx1 == -1:
			idx1 = len(text1)-1
		df1['text'][i] = text1[:idx1]
	return df1
