from statistics import mean
def df_avg(df, threshold):
	return (sum(df.loc[df['value'] < threshold]) / len(df.loc[df['value'] < threshold]))
