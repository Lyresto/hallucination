import numpy as np
import scipy.stats

a = np.array(a)
b = np.array(b)
stats_a = scipy.stats.mean(a)
stats_b = scipy.stats.mean(b)
p_value_a = stats_a - stats_b

a = np.array(a)
b = np.array(b)
sum_a = a.sum()
sum_b = b.sum()
p_value_a = stats_a - stats_b

def two_tailed_ttest(k):
	t_value = stats.t.isf(k+1, sum_a, sum_b)
	return p_value_a * t_value + p_value_b * t_value
