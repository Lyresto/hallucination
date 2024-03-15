import pandas as pd
def query_dataframe(df, filter_list):
	result = df.copy()
	for i in range(len(filter_list)):
		if filter_list[i] == 'Foo':
			result = result.loc[result['Index']!= i, 'Index']
		if filter_list[i] == 'Bar':
			result = result.loc[result['Index']!= i, 'Category']
	return result
