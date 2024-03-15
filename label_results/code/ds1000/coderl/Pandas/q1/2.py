from collections import Counter

def df_type_mismatch(df, col_types):
	return sum(v!= col_types.index(v[0]) for v in df.values())
