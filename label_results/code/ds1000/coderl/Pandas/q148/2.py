from pandas import groupby

def pd_series_sum(series, skipna=False):
	if skipna:
		return sum(series)
	else:
		try:
			return sum(series.sum(skipna=True))
		except TypeError:
			try:
				return sum(series.sum())
			except TypeError:
				try:
					return sum(series.apply(lambda x: np.sum(x)))
				except TypeError:
					return sum(series)
