def duplicates(df):
	duplicates = df.duplicated(subset=['col1','col2'], keep='first')
	return duplicates
