import numpy as np
def check_columns_uniquity(df1, df2):
	columns_check_list = ['A','B','C','D','E','F'] 
	check = np.where([df1[column]!= df2[column] for column in columns_check_list]) 
	return [np.all(check) for column in columns_check_list]
