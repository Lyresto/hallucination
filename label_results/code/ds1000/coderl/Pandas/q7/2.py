# import pandas as pd
# df = pd.DataFrame({'url': ['A.com', 'A.com', 'A.com', 'B.com', 'B.com', 'C.com', 'B.com'],
#                   'keep_if_dup': ['Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes']})
# result =... # put solution in this variable

import collections

def drop_duplicates(df, keep_if_dup=True):
	d = collections.defaultdict(list)
	for i in df:
		d[i[1]].append(i[0])
	
	for i in d:
		d[i]=sorted(d[i])
	
	result = []
	for i in d:
		if keep_if_dup:
			if d[i].index(i) > 1:
				result.append([i, d[i][0], d[i][1]])
		else:
			if d[i].index(i) == 1:
				result.append([i, d[i][0], d[i][1]])
	return result
