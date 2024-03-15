def rename_columns(df):
	return df.rename(columns={'Header' + k: k + str(len(k)) for k in range(len(df.columns))})
