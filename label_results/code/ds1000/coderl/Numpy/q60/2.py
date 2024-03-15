import numpy as np
import scipy.stats

a = np.array(a)
b = np.array(b)
mean1 = a.mean()
mean2 = b.mean()
stds1 = (a - mean1) ** 2 + (b - mean2) ** 2
p_value = scipy.stats.ttest_1samp(a,b)[1]

