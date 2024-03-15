from statistics import mean
def threshold_df_agg(df, threshold):
	result = df.value.copy()
	for key, group in df.groupby('lab'):
		if mean(group)>=threshold:
			result = result.replace(key,'',1)
	return result
