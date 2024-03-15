def f(df=example_df):
	for i,j in df.iterrows():
		df.loc[i,'Title']=df.loc[i,'Title'].replace("&","&amp;").replace("&","&amp;")
	return df
