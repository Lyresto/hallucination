import pandas as pd
df = pd.DataFrame({'name': ['Aaron', 'Aaron', 'Aaron', 'Brave', 'Brave', 'David'],
	'a': [3, 3, 3, 4, 3, 5],
	'b': [5, 6, 6, 6, 6, 1],
	'c': [7, 9, 10, 0, 1, 4]})
for i in range(len(df['a'])):
	df['a'][i] = str(i+1)
#df.to_string(header='name  a  b   c')
print(df)
