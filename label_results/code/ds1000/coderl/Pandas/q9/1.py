from collections import Counter

def drop_duplicates(df, keep_if_dup=False):
	dct = dict(Counter(df['url']))
	return '\n'.join('{}     {}     {}'.format(k, v, 'Yes' if v==keep_if_dup else 'No') for k,v in dct.items())
