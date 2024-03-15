from datetime import datetime
def parse_df(df):
	for i, row in enumerate(df.itertuples(), 1):
		df.index.levels[i] = datetime.strptime(row[1], '%Y/%m/%d')
	return df
