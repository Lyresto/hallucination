from collections import OrderedDict

def drop_duplicates(df, keep_if_dup='YES'):
	return "\n".join([f"{i}    {df[i]['url'] }   {df[i]['keep_if_dup']}"
					  for i in sorted(df.columns) if (df[i].keep_if_dup == keep_if_dup)])
