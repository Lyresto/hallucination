import pandas as pd

def sort_df(df):
	for col in df:
		df[col] = df[col].sort_values(by=lambda x: x[1])
	return df
