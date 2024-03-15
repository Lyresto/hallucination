from collections import defaultdict

def find_duplicates(df):
	d = defaultdict(list)
	for x, i in df.items():
		d[i].append(x)
	return [x for x, i in d.items() if len(i) > 1]
