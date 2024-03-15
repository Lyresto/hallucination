from collections import defaultdict
import pandas as pd

d = defaultdict(list)
for col in ['group', 'group_color', 'val1', 'val2', 'val3']:
	d[col] = [5,2,3,4,5,7]

def aggregate(df, col):
	if col not in d:
		return 0
	return sum(df[col])

df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B'], 'group_color' : ['green', 'green', 'green', 'blue', 'blue'], 'val1': [5, 2, 3, 4, 5], 
'val2' : [4, 2, 8, 5, 7],
'val3': [1,1,4,5,1],
'val4': [4, 2, 8, 5, 7],
'val5': [4, 2, 8, 5, 7],
'val6': [4, 2, 8, 5, 7],
'val7': [4, 2, 8, 5, 7],
'val8': [5, 2, 3, 4, 5],
'val9': [5, 2, 3, 4, 5],
'val10': [5, 2, 3, 4, 5],
'val11': [5, 2, 3, 4, 5],
'val12': [4, 2, 8, 5, 7],
'val13': [4, 2, 8, 5, 7],
'val14': [5, 2, 3, 4, 5],
'val15': [4, 2, 8, 5, 7],
'val16': [4, 2, 8, 5, 7],
'val17': [5, 2, 3, 4, 5],
'val18': [4, 2, 8, 5, 7],
'val19': [4, 2, 8, 5, 7],
'val20': [5, 2, 3, 4, 5],
'val21': [4, 2, 8, 5, 7],
'val22': [4, 2, 8, 5, 7],
'val23': [4, 2, 8, 5, 7],
