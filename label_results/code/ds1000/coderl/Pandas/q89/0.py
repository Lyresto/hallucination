import pandas as pd
df1 = pd.DataFrame({'A': [1, 1, 1],
				  'B': [2, 2, 2],
				  'C': [3, 3, 3],
				  'D': [4, 4, 4],
				  'E': [5, 5, 5],
				  'F': [6, 6, 6],
				  'Postset': ['yes', 'no']})
df2 = pd.DataFrame({'A': [1, 1, 1],
				 'B': [2, 2, 2],
				 'C': [3, 3, 3],
				 'D': [4, 4, 4],
				 'E': [5, 5, 5],
				 'F': [6, 6, 6],
				 'Postset': ['yes', 'no']})
columns_check_list = ['A','B','C','D','E','F']
def check_column_uniqueness(df1,df2):
	result = []
	for column in columns_check_list:
		check = np.where([df1[column]!= df2[column] for column in columns_check_list]) 
		if len(check) > 0:
			result.append(check[0][0])
	return result
