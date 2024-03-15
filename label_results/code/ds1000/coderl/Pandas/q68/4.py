def df_mask(df, c):
	cols = [col for col in df.columns if col > c]
	return df[cols]
