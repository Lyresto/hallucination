from collections import Counter

def percentage(df):
	categories = Counter(df["cat"])
	return 0 if not categories else sum(1/len(categories[cat]) for cat in categories)
