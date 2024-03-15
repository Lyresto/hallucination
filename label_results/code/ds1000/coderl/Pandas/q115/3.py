def percent_of_category(df):
	total = len(df['cat'])
	return 1 - sum(v/total for v in df['val1']) / total
