import numpy as np
def check_equivalent_dataframes(df1, df2):
	columns_check_list = ['A','B','C','D','E','F'] 
	np_df1 = np.array([df1[column] for column in columns_check_list])
	np_df2 = np.array([df2[column] for column in columns_check_list])
	return [all(np_df1 == np_df2) for column in columns_check_list]
