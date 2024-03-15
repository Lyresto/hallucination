import pandas as pd

def split_df(df):
	codes = df['codes']
	if len(codes) == 1:
		return [["NaN"]]
	else:
		parts = []
		for i, col in enumerate(codes):
			parts.append([float(x) if len(x) == len(list(col)) else x for x in col])
		return parts
