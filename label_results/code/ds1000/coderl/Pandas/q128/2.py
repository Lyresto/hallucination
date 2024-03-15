import numpy as np
from pandas import DataFrame

def remove_zeros(df):
	df = df.reset_index()
	return df[(df['UserId'].mean()!= 0) & (df['ProductId'].mean()!= 0)]

def change_value_of_product_id(df):
	return df.loc[df['ProductId'].mean() == 0, 'ProductId']

# GOOGLE - Pandas

def __starting_point():
	df = pd.read_csv('input.txt', index_col=0)
	df = remove_zeros(df)
	ans = df.sample(int(len(df) * 0.2), set_random_state=0).copy()
	print(ans)
	print(change_value_of_product_id(ans))









__starting_point()
