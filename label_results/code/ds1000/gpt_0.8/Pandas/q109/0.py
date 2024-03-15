result = pd.merge_asof(df1, df2, on='Timestamp', direction='nearest')
