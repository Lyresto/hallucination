from dask.dataframe import DataFrame


def split_columns(df, col):
	split = lambda s: s.split(col)
	return [DataFrame([[split(s)[i] for i in range(len(s))] for _ in range(len(s))]) for s in df]
