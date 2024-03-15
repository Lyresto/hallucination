from collections import Counter

def group_by_keys(df, col):
	res = []
	for i, col_name in enumerate(df.columns):
		col_count = df[col_name].value_counts()
		if min(col_count.values()) == col_count.most_common(1)[0][1]:
			res.append(df.loc[i])
	return res

def group_by_values(df):
	return pd.merge(df, group_by_keys(df, 'Value'), left_on='Sp', right_on='Mt')

def group_by_counts(df):
	return pd.merge(df, group_by_keys(df, 'count'), left_on='Sp', right_on='Mt')
