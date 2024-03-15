from numpy import array

def subset_rows_and_columns(df):
	cols = list(df.columns)
	subset = df[df.c > 0.5]
	return array([subset[col] for col in cols])
