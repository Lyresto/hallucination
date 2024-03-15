import pandas as pd
def duplicate_rows(df):
	# write your code here
	df = df.drop_duplicates('col1', keep='last')
	df['col1'] = [i[0] for i in df.col1]
	df['col2'] = [i[1] for i in df.col2]
	return df
