def combine_names_and_a(df):
	df_new = df.copy()
	for i in range(len(df['name'])):
		df_new['name'][i] = str(i+1)
	
	return df_new
