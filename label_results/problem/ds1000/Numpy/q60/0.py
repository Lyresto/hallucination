a = a[~np.isnan(a)]
b = b[~np.isnan(b)]
t, p_value = scipy.stats.ttest_ind(a, b, equal_var=False)
