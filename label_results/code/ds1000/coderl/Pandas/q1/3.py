from collections import Counter

def how_many_rows_have_different_Type_than_origin(df: pd.DataFrame):
	types = Counter(df['Type'])
	return sum(count!= types[x] for x, count in types.items())
