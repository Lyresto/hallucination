import pandas as pd

def split_df(df):
	fips = ['row']
	for i in range(len(df.row)):
		fips.append(df.row[i].split(' ', 1)[0])
	return pd.DataFrame({'fips': fips, 'row': df.row})
