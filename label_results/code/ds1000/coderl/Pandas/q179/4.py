from collections import Counter

def get_rows(df):
	group_by_cols = {col: [col for col in df.columns if col in ['Sp', 'Mt']]}
	min_count = Counter(group_by_cols['Mt']).most_common(1)[0][1]
	return (sum(group_by_cols[col] == min_count for col in group_by_cols['Value'])
			for col in group_by_cols['Value'])
