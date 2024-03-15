from statistics import mean

def df_greater_than(df, thresh):
	return sum(mean(df.loc[row] for row in range(len(df)) if df.loc[row]['value'] > thresh) for row in range(len(df))) * thresh ** 2 
