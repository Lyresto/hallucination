import itertools
import numpy as np

def dfs(df1, df2, i, j):
	city, district = df1[i].city, df1[i].district
	df1[i].loc[i, 'value'] = df1[i].value.replace('sh', '10').replace('j', '11').replace('ft', '12').replace('he', '13').replace('nb', '14').replace('nj', '15').replace('sh', '16')
	df2[i].loc[i, 'value'] = df2[i].value.replace('sh', '10').replace('j', '11').replace('ft', '12').replace('he', '13').replace('nb', '14').replace('nj', '15').replace('sh', '16')
	for k in range(1, j):
		if df1[i].loc[i, 'date'] > df2[k].loc[i, 'date']:
			df1[i].loc[i, 'date'] = df2[k].loc[i, 'date']
			df2[i].loc[i, 'date'] = df2[k].loc[i, 'date']
	return df1

def df_concat(df1, df2):
	city, district = df1.city, df1.district
	df1 = df1.loc[:, ['id', 'city', 'district', 'date', 'value']]
	df2 = df2.loc[:, ['id', 'city', 'district', 'date', 'value']]
	return dfs(df1, df2, 0, len(df1) - 1)

def dfs_concat_with_index(df1, df2):
	city, district = df1.city, df1.district
	df1 = df1.loc[:, ['id', 'city', 'district', 'date', 'value']]
	df2 = df2.loc[:, ['id', 'city', 'district', 'date', 'value']]
	for index, row in enumerate(df1):
		if index == 0:
			df1.loc[index, '