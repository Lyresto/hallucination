df = pd.melt(df, id_vars=['user', 'someBool'], var_name='date', value_name='value')
df = df.dropna(subset=['value'])
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y')
df = df.sort_values(['user', 'date'])
