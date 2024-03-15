import scipy.stats
a = np.array(a)
b = np.array(b)
c = a + b
mean = c.mean()
sd = c.std()
p_value = scipy.stats.ttest_ind(c,mean)/sd
