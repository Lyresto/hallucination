import pandas as pd

def max2(df):
	rows = []
	for i, row in enumerate(df.values):
		if max(row) == 2:
			rows.append(i)
	return rows

def end_solution(df):
	res = []
	for i, col in enumerate(df.columns):
		if len(max2(df.values[:i])) == 2:
			res.append('{}  {}  {}  {}'.format(col, '0', '0', '0'))
		elif len(max2(df.values[:i])) > 2:
			res.append('{}  {}  {}  {}'.format(col, '0', '1', '1'))
		else:
			res.append('{}  {}  {}  {}'.format(col, '0', '0', '1'))
	return '\n'.join(res)
