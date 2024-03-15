import pandas as pd


def sort_index(df):
	result = {}
	for i, row in df.iterrows():
		sort_idx = pd.to_datetime(row['TIME'])
		result[i] = sort_idx.year * 100 + sort_idx.month * 10 + sort_idx.day
	return result

df['RANK'] = df['TIME'].rank().sort_values(by='RANK', ascending=False)
