from collections import defaultdict
from itertools import groupby

def group_by_value(df):
	return {k: list(v) for k, v in groupby(df['Value'], key=lambda x: int(x))}

def count_max(df):
	return df.groupby('Value').count().dropna()

def solution(df):
	return list(map(count_max, group_by_value(df)))
