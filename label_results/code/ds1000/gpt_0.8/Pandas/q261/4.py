df['TIME'] = pd.to_datetime(df['TIME'])  # Convert TIME column to datetime format
df['RANK'] = df.groupby('ID')['TIME'].rank(ascending=False)  # Add rank column based on ID and time
df['TIME'] = df['TIME'].dt.strftime('%d-%b-%Y %a %H:%M:%S')  # Change format of TIME column
