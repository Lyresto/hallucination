from collections import Counter
from itertools import chain

def multi_index_series(df):
	categories = df.columns.values
	times = list(df.index.values)
	return [[sum(1 for _ in col_time_series(df[i], col)) for i, col_time_series in enumerate(zip(categories, times))] for col in df.columns]
	
def sum_series(series, col_index):
	return sum(series[col] for col in col_index)

def col_time_series(df, col):
	return chain(df[col].tolist(), df.loc[col].tolist())
