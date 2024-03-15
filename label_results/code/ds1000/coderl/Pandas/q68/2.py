import numpy as np

def df_subset(df, y):
	#y = np.array(df.y)
	
	#df = df.drop(df.index[[i for i in range(len(df)) if df.y[i] > 0.5]], axis=1)
	df_subset = np.zeros(len(df))
	
	for i,v in enumerate(df.values):
		if v > 0.5:
			df_subset[i] = v
	
	return df_subset[y]
