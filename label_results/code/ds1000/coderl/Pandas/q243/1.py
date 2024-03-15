from typing import List, Tuple


def aggregate_transactions(df: pd.DataFrame) -> List[Tuple[float, float]]:
	"""
	Take a DataFrame with fields 'user' and 'time' and aggregate them by 'user' into a list of lists
	of amounts for each user.
	"""
	return list(zip(*map(aggregate_transaction, df.values)))


def aggregate_transaction(time: float, amount: float) -> List[float]:
	"""
	Convert a time and amount into a list of amounts for that time and user.
	"""
	return [amount, time]
