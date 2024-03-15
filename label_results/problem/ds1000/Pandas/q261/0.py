# Convert TIME column to datetime format
df['TIME'] = pd.to_datetime(df['TIME'])

# Add a new column for formatted time
df['FORMATTED_TIME'] = df['TIME'].dt.strftime('%d-%b-%Y %a %H:%M:%S')

# Add a new column for ranking by ID and TIME
df['RANK'] = df.groupby('ID')['TIME'].rank(ascending=False)
