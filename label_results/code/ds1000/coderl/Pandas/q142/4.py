import pandas as pd
def melt(df, value_vars):
	result = [list(i) for i in zip(df.columns[::-1],
						 df.columns[1::-1])]
	for i in range(len(df.columns)):
		result[i] = list(zip(*value_vars))[i%6]
	return pd.DataFrame(result).T
