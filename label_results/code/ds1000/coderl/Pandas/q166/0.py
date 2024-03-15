def stdMeann(df):
	s = [0]*len(df)
	for i in range(len(df)):
		s[i] = df['b'].mean()
		s[i+1] = df['b'].std()
	return pd.Series(s)
