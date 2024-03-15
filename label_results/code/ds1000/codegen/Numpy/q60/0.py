import numpy as np
import scipy.stats
a = np.random.randn(40)
b = 4*np.random.randn(50)
p_value = scipy.stats.ttest_1samp(a,b)
