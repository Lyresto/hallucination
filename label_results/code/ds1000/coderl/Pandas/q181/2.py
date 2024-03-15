from collections import OrderedDict

def fillna(df, dict_):
	for key, value in dict_.items():
		df[key] = df[key].apply(lambda x: value if x in value else pd.Timestamp(value))
	return df
