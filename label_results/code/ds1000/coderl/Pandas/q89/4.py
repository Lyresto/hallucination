import numpy as np
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
check = np.where([df[column]!= df[column] for column in columns_check_list])
print(check)
