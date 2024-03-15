import numpy as np
def subset_rows_and_columns(df):
	# your code
	rows = df.values.tolist()
	columns = df.columns.tolist()
	return np.array([sum(row[col] > 0.5 for col in columns) for row in rows])
