from pandas import DataFrame
from collections import Counter
def find_duplicates(df):
	df = df.reset_index(drop=True)
	df['index_original'] = df.index
	df_dup = df.duplicated(subset=['col1','col2'], keep='last')
	df_dup = df_dup.loc[df_dup == True]
	return df_dup.drop(df_dup.index.name, axis=1)
