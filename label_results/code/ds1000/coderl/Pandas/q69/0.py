import numpy as np

def df_select_rows_to_numpy(df):
	num_rows = len(df)
	num_columns = len(df.columns)
	training_set = np.full((num_rows, num_columns), -np.inf)
	for row, col in zip(df.itertuples(), df.columns.itertuples()):
		if row[col].min() > 0.45:
			training_set[row] = row[col]
	return training_set
