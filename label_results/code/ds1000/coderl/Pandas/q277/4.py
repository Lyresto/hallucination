from pandas import pd
def sort_index(df):
	return df.sort_index(key=lambda r:r['time'])
