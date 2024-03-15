from math import ceil
def fillna(df, n = 8000):
	for i in range(n):
		if(df.iloc[i]==0):
			df['Column_x']=0
		elif(df.iloc[i]==1):
			df['Column_x']=1
		else:
			df['Column_x']=1
			df.iloc[i]=0
			break
