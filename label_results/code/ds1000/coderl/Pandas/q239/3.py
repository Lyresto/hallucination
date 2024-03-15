from itertools import chain
from pandas.io.formats import df_to_sql

def dfs_concat(df1, df2):
	df = df1.append(df2, ignore_index=True)
	df = chain.from_iterable((df[a] for a in range(1, len(df)) if df[a].year < df[b].year), fillvalue=None)
	return df.to_sql(index=False, dtype={'id': str, 'city': str, 'district': str, 'date': str, 'value': str})
