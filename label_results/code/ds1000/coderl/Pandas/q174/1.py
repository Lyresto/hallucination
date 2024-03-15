from collections import OrderedDict
import re


def df_series_by_value(series):
	series_values = [int(i) for i in re.findall('\d+', series.index)]
	ordered_values = OrderedDict.fromkeys(series_values)
	return series.sort_values(key=lambda x: ordered_values[x])
