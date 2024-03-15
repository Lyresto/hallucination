from collections import defaultdict
from itertools import groupby

def solve(df):
	vals = list(df['Value'])
	cols = list(df.columns)
	dct = defaultdict(list)
	for idx, col in enumerate(cols):
		dct[col].append(idx)

	res = []
	for key, group in groupby(df, key = 'Value'):
		res.append(
			list(
				zip(
					group.sort_values(by='count').values,
					group.index
				)
			)
		)
	return res
