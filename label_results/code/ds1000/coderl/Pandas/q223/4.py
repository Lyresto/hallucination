def fillna(df, r=0.5):
	for i in range(len(df.columns)):
		if(df.columns[i]==None):
			continue
		df.columns[i] = df.columns[i].fillna(df.mode()[r%len(df.columns)],inplace=True)
