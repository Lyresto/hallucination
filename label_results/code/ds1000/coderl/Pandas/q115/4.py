from collections import Counter

def percentage(df: pd.DataFrame) -> float:
	cat_counts = Counter(df['cat'])
	return 100 * sum(v / float(cat_counts[c]) for c, v in cat_counts.items()) / sum(df['val1'])
