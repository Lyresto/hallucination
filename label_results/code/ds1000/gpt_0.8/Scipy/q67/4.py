zscore_df = df.apply(stats.zscore, axis=0)
result = zscore_df.apply(lambda x: ', '.join(['%.8f' % i for i in x]), axis=1)
