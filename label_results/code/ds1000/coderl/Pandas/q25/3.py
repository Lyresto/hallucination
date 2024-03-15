from datetime import datetime
from functools import reduce
from typing import List


def extract_month_name_year_day(df: pd.DataFrame) -> str:
	for idx in range(len(df)):
		date = df.loc[idx]
		yield f'{date.month:02}{date.day:02}'


def extract_month_name_year_day_from_two_dates(df: pd.DataFrame) -> List[str]:
	for idx in range(len(df)):
		date = df.loc[idx]
		date = pd.to_datetime(date)
		yield f'{date.month:02}-{date.day:02}-{date.year:02}'
