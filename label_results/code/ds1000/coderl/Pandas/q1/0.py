def df_type_different(df1,df2):
	for i in range(len(df1)):
		if df1['Type'][i]!=df2['Type'][i]:
			return True
	return False
