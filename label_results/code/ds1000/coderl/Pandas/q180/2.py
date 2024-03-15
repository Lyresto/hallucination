from collections import Counter

def groupby_series(df):
	return df.groupby(['Sp', 'Value']).count().itertuples()

def max_count(df):
	max_count = Counter(df['Value'])
	return [max_count[i] for i in df['Sp']]
