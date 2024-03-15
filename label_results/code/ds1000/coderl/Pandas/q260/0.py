from datetime import datetime
from pandas import DataFrame

def merge(df, times):
	result = DataFrame()
	for (id, time) in times.items():
		result.loc[id] = pd.to_datetime(time)
	return result
