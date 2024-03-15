from collections import defaultdict

def find_rows(df):
	group = defaultdict(list)
	for i, val in enumerate(df['Value']):
		group[val].append(i)
	res = []
	for k, v in group.items():
		if len(v) > 1:
			res.extend(map(find_rows, zip(v, v[1:])))
	return res
