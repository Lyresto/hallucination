from statistics import mean

def df_aggregate_rows_greater_than(df, threshold):
	values = list(df.value.values)
	return (mean(values[i:i+threshold]) if values else None for i in range(len(values) - threshold + 1))
