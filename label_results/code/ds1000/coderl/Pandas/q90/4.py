import pandas as pd
df1 = pd.DataFrame({'A': [1, 1, 1],
				   'B': [2, 2, 2],
				   'C': [3, 3, 3],
				   'D': [4, 4, 4],
				   'E': [5, 5, 5],
				   'F': [6, 6, 6],
				   'Postset': ['yes', 'no', 'yes']})
df2 = pd.DataFrame({'A': [1, 1, 1],
				   'B': [2, 2, 2],
				   'C': [3, 3, 3],
				   'D': [4, 4, 4],
				   'E': [5, 5, 5],
				   'F': [6, 6, 6],
				   'Postset': ['yes', 'no', 'yes']})
columns_check_list = ['A', 'B', 'C', 'D', 'E', 'F']
result = []
for i in columns_check_list:
	for j in columns_check_list:
		result.append(df1[i] == df2[j])
print(result)
