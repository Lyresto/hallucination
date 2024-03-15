def sort_by_time(df):
	# your code here
	df.sort_index(key=lambda x:x['time'])
	return df
