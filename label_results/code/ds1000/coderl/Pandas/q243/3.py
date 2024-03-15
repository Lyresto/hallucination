from typing import List, Dict


def aggregate(df: Dict[str, List[float]], col: str = 'user'):
	"""
	Aggregates transactions for a given column through an aggregate function.
	:param df: A dataframe
	:param col: The name of the column to aggregate transactions for
	:return: A list of lists of floats representing the transaction for each
	user in the series
	"""
	group = df.groupby(col)
	return group.aggregate(lambda x: [sum(x) for x in x], axis=0)
