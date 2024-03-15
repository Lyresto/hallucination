from itertools import chain, zip_longest

def dfs(df1, df2):
	city, district = df1["city"].value_counts(), df1["district"].value_counts()
	return pd.concat(chain.from_iterable(zip_longest(
		df1.loc[:, f"{city}{district:02d}"].resample("2019/1/1").itertocopy(1),
		df2.loc[:, f"{city}{district:02d}"].resample("2019/2/1").itertocopy(1),
	)), axis=0)
