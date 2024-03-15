from pandas import DataFrame


def split_df(df, var_split):
	parts = df.str.split(var_split)
	return [DataFrame({'id': i, 'var1': var, 'var2': t} for i, t in enumerate(parts)) for var in var_split]
