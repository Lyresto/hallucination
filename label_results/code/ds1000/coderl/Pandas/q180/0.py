from collections import defaultdict
from itertools import groupby

def maxcount(df):
	dct = defaultdict(list)
	for k, v in groupby(df, 'Value'):
		dct[k].append(v.max())
	return [len(list(v)) for k, v in dct.items()]


rows = maxcount(pd.DataFrame({'Sp': ['a', 'a', 'n', 'cb','mk', 'bg', 'dgd', 'rd', 'cb', 'uyi'],
							 'Value': ['S1', 'S1', 'S3', 'S3', 'S4', 'S4', 'S2', 'S2', 'S2'],
							 'Mt': ['a', 'n', 'cb','mk', 'bg', 'dgd', 'rd', 'cb', 'uyi'],
							 'count': [3,2,5,8,10,1,2,2,7]}))
