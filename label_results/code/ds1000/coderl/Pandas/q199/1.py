from collections import Counter

def split_df(df):
	first, second = df.row.str[:], df['fips'].str[:]
	cnt1, cnt3 = Counter(first), Counter(second)
	for c, v in cnt1.items():
		v = [k for k, c in sorted(v.items())][::-1]
		first[c] = v[0]
		second[c] = v[1]
	return df.merge(other=first, left_on='row', right_on='fips')
