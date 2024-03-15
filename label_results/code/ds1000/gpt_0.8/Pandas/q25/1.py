df = df[(df['Date'] >= List[0]) & (df['Date'] <= List[1])]
df['Month'] = df['Date'].dt.strftime('%b')
df['Year'] = df['Date'].dt.strftime('%Y')
df['Day'] = df['Date'].dt.strftime('%A')
df['Date'] = df['Month'] + '-' + df['Year'] + ' ' + df['Day']
df = df[['Date']]
