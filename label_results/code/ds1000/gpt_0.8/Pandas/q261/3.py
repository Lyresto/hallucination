df['TIME'] = pd.to_datetime(df['TIME'])
df['RANK'] = df.groupby('ID')['TIME'].rank(ascending=False)
df['TIME'] = df['TIME'].dt.strftime('%d-%b-%Y %a %H:%M:%S')
