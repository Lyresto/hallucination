import pandas as pd

def split_df(df):
	df['row'] = df['row'].str.split(" ", 1)
	df['fips'] = df['row'].map("".join)
	return df
