import numpy as np
from itertools import cycle

def remove_duplicate_rows(df):
	df_copy = df.copy()
	counts = np.array(df_copy['UserId'].value_counts())
	num_perc = counts / float(len(df_copy['UserId']))
	for i in cycle(range(len(df_copy['UserId']))):
		df_copy['UserId'][i] = 0
		counts[i] = 0
	return df_copy
	
def change_product_id_to_zero(df):
	df['ProductId'] = df['ProductId'].apply(lambda x: x - 1)
	return df
