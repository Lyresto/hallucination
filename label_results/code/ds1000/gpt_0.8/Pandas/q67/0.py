df = pd.melt(df, id_vars=['user', 'someBool'], var_name='date', value_name='value')
df = df.dropna() # remove rows with missing values
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y') # convert date column to datetime format
df = df.sort_values(by=['user', 'date']) # sort by user and date
df = df.reset_index(drop=True) # reset index
