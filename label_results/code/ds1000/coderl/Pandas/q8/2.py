from collections import OrderedDict

def drop_duplicates(df, drop_if_dup='Yes'):
	print((df.copy().drop_duplicates(subset='url', keep=drop_if_dup).reset_index()))
	return df.copy().drop_duplicates(subset='url', keep=drop_if_dup).reset_index()
