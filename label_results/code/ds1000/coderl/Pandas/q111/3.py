def state(df):
	for i in range(len(df)):
		if df[i]['col2'] > 50 or df[i]['col3'] > 50:
			return df[i]['col1']
