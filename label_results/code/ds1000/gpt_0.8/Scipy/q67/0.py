zscore = stats.zscore(df, axis=0)
result = pd.DataFrame(zscore, index=df.index, columns=df.columns)
