from collections import OrderedDict

def drop_duplicates(df, keep_if_dup=True):
	d = OrderedDict()
	for row in df:
		k = row.get("keep_if_dup", None)
		if k is not True:
			d[row["id"]] = k
			d[row["url"]] = k
	return df.merge(d, left_on="id", right_on="url", how="left")
