from collections import defaultdict

def find_duplicated_rows(df):
	df = df.sort_values(by=['col1', 'col2'])
	result = defaultdict(list)
	for row in df:
		result[row[0]].append(row[1])
	for col in result:
		result[col].sort()
	for row, col_index in result.items():
		df.loc[row, col] = df.loc[col, col_index].values.pop()
	return df
