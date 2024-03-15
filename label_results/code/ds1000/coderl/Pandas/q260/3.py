import pandas as pd
from collections import defaultdict

def rank(df):
	d = defaultdict(list)
	for i, j in df.iterrows():
		d[i].append(int(j[:8]))
	return pd.DataFrame(d).sort_values('TIME').index.values.tolist()
