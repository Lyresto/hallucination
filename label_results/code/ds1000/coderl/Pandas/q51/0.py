def df_exp(df,col,prefix):
	ans = ""
	for i in df.columns:
		if i == col:
			ans += prefix+"_"+str(i)
		else:
			ans += prefix+"^"+str(i)
	return ans
