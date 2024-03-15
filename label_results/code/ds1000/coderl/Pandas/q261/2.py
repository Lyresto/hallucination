from datetime import datetime
from typing import List, Dict, Set


def rank_by_time(df: Dict[str, List[str]], sort_by: str = 'TIME') -> Dict[str, List[int]]:
	return pd.rolling_sum(df, sort_by) \
		.map(lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), 1)) \
		.sort_values(by=sort_by)
