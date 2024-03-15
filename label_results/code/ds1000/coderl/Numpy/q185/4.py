# write the function df_cum
def df_cum(df, n):
	if n == 'Q':
		return df[n]
	else:
		return df[str(n)]
