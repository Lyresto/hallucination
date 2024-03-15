from itertools import zip_longest
from typing import List
import pandas as pd


def pivot_table(df: pd.DataFrame, pivot_by: List[str] = ['user', 'date', 'value'], output_columns: List[str] = ['user', 'date', 'value','someBool']):
	# x-array = list(zip_longest(*([df.ix[:, x] for x in range(0, len(df))], fillvalue=0)))
	x-array = df.pivot(index='user', columns=pivot_by, values='date')
	y-array = df.pivot(index='date', columns=pivot_by, values='value')
	return pd.concat(xarray, yarray, axis=1, join='outer')
