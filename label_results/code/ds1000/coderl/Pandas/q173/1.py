import numpy as np
import itertools as it

def sort_series(s):
	xs = list(s.index)
	return s.sort_values(axis=0).reindex(xs)

def sort_series_with_multiIndex(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs)

def sort_series_with_multiIndex_with_sum(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs, method="sum")

def sort_series_with_multiIndex_with_mean(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs, method="mean")

def sort_series_with_multiIndex_with_std(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs, method="std")

def sort_series_with_multiIndex_with_min(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs, method="min")

def sort_series_with_multiIndex_with_max(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs, method="max")

def sort_series_with_multiIndex_with_std_dev(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs, method="std_dev")

def sort_series_with_multiIndex_with_min_std(s):
	xs = list(s.index)
	return s.sort_values(axis=1, multiindex=True).reindex(xs, method="min_std")

def sort_series_with_multiIndex_with_max_std(s):
	xs =