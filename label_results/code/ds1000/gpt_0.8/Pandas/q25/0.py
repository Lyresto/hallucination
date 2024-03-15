df = df[(df['Date'] >= List[0]) & (df['Date'] <= List[1])]
df['Month'] = df['Date'].dt.month_name().str.slice(stop=3)
df['Year'] = df['Date'].dt.year
df['Day'] = df['Date'].dt.day_name().str.slice(stop=3)
df['Date'] = df['Month'] + '-' + df['Day'] + '-' + df['Year'].astype(str)
df = df[['Date']]
