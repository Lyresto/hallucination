import pandas as pd
from operator import itemgetter

def sort_df(df):
	result = []
	for k, g in df.groupby('cokey'):
		a, b = zip(list(g.sort_values()), list(g.sort_values()))
		result.append([k, a, b])
	return pd.DataFrame.from_dict(result).sort_values('A')
