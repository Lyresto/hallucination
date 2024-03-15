import pandas as pd

def rename_columns(df):
	df = df.copy()
	for i in range(len(df['HeaderA'])):
		if df['HeaderA'][i].endswith('X'):
			df['HeaderA'][i] = df['HeaderA'][i][:-1] + 'X'
	return df
