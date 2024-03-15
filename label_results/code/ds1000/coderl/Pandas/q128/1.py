import numpy as np

def normalize(df):
	df['ProductId'] = df['ProductId'].astype(int)
	df['Quantity'] = df['Quantity'].astype(int)
	df = np.divide(df, np.array(df['Quantity']).sum())
	df = df.astype(int)
	return df
