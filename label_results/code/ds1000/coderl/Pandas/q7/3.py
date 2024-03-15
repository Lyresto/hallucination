from collections import Counter
def drop_duplicates(df, keep=True):
	df=df.copy()
	for i in range(len(df)):
		if keep==True and i!=df.loc[i]['url']:
			df.loc[i]=df.loc[i].copy()
	return df.loc['id','url','keep_if_dup']
