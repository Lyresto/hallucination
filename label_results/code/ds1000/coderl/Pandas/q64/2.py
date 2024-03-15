from itertools import zip_longest
from collections import OrderedDict

def get_df():
	return pd.DataFrame(OrderedDict.fromkeys(zip_longest(df['a'], df['name']), index=range(len(df['a']))))
	
def solution():
	return '\n'.join(['{}  {}   {}'.format(*row) for row in get_df().itertuples()])
