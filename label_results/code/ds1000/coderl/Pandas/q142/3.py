import pandas as pd
def melt(df, value_vars):
	# your code here
	if len(value_vars) == 0:
		return df
	else:
		result = pd.DataFrame()
		for i, v in enumerate(value_vars):
			for j, k in enumerate(v):
				result[f"col{i}{j}"] = df[k]
		return result
