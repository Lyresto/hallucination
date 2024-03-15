import pandas as pd

def sort_df(s):
	# your code here
	series = pd.Series(s)
	series.sort_values(inplace=True)
	index = series.index
	new_series = pd.Series(index)
	new_series.sort_values(inplace=True)
	return new_series
	
