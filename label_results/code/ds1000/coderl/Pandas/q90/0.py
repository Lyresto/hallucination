import numpy as np

def check_unique_columns(df1, df2):
	columns_check_list = ['A', 'B', 'C', 'D', 'E', 'F']
	np_columns_check = np.where([df1[column] == df2[column] for column in columns_check_list])
	return [np_columns_check[0][0] == 0 for _ in range(len(columns_check_list))]
