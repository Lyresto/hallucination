from typing import Dict, List, Tuple
from copy import deepcopy

def f(dict: Dict[str, str], df: pd.DataFrame):
	# return the solution in this function
	d = deepcopy(dict)
	for i, j in enumerate(df.columns):
		df.loc[i, j] = df.loc[j, j].fillna(d.get(j, j))
	return df
