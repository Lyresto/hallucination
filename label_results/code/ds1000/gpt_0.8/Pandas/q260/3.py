df['TIME'] = pd.to_datetime(df['TIME']) # convert TIME column to datetime format
df['RANK'] = df.groupby('ID')['TIME'].rank(ascending=False) # calculate rank by grouping ID and ranking TIME column
