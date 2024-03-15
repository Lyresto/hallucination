from operator import itemgetter
from itertools import zip_longest

def pivot_table(df):
	p_col = list(df.keys())[0]
	p_date = list(df[p_col].dt.date)
	p_bool = df[p_col].apply(lambda x: bool(x) if x is not None else False)
	return pd.DataFrame(dict(zip_longest(p_date, p_bool, fillvalue=None)))
