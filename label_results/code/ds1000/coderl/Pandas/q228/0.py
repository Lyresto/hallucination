def cycle(df):
	return (tuple(df[col].values.tolist() if len(df) == 1 else (np.nan,)*len(df)) for col in df.columns)
