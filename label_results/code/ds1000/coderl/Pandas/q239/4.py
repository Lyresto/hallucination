from datetime import date
def dfs(df1, df2):
	df3 = df1.copy()
	for i in range(len(df2)):
		if (df2.loc[i]['city'], df2.loc[i]['district'])!= ('j','1'):
			df3.loc[i,'date'] = df2.loc[i]['date'].map(lambda x: date(int(x[:4]),int(x[5:7]),int(x[8:10])).strftime("%Y/%m/%d"))
	for i in range(len(df1)):
		if (df1.loc[i]['city'], df1.loc[i]['district'])!= ('j','1'):
			df3.loc[i,'date'] = df1.loc[i]['date'].map(lambda x: date(int(x[:4]),int(x[5:7]),int(x[8:10])).strftime("%Y/%m/%d")
	df4 = df2.copy()
	for i in range(len(df1)):
		if (df1.loc[i]['city'], df1.loc[i]['district'])!= ('j','1'):
			df4.loc[i,'date'] = df1.loc[i]['date'].map(lambda x: date(int(x[:4]),int(x[5:7]),int(x[8:10])).strftime("%Y/%m/%d")
	return df3.append(df4,ignore_index=True)
