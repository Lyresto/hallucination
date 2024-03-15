def __starting_point():
	df = pd.DataFrame([[1,2,3,1],[0,0,0,0],[1,0,0,1],[0,1,2,0],[1,1,0,1]],columns=['A','B','C','D'])
	print(df)
	result = df.copy()
	for i in range(len(result)):
		for j in range(len(result[i])):
			if df.iloc[i][j] == 2:
				result.loc[i,j] = 0
				break
	for j in range(len(result.columns)):
		for i in range(len(result.rows)):
			if df.columns[j] == 2:
				result.columns[j] = 0
				break
	print(result)


__starting_point()
