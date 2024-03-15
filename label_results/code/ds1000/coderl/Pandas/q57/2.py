import pandas as pd

def min_max_expand(df):
	#your code here
	min_dt = min(df['dt'])
	max_dt = max(df['dt'])
	index = df['dt'].str.index('2022-01-')
	res = {k: [0 for i in range(len(df.columns))] for k in range(len(df.columns))}
	for i in range(len(df.columns)):
		res[i][index[i]] = df.val[i]
	for i in range(len(df.columns)-1, -1, -1):
		if df.dt[i] > max_dt:
			res[i][index[i]] = 0
		elif df.dt[i] < min_dt:
			res[i][index[i]] = 0
	return res
