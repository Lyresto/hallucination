result = pd.merge_asof(df2, df1, on='Timestamp', direction='backward')
