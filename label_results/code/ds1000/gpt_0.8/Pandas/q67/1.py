# Melt the date columns into rows
df = pd.melt(df, id_vars=['user', 'someBool'], var_name='date', value_name='value')

# Drop rows with missing values
df = df.dropna()

# Convert date column to datetime type
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y')
