def percentage(df):
	res = 0
	for i in df:
		res += i/len(df['cat'])
	return res/100
