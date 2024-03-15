df = df[df['Date'].isin(pd.date_range(start=List[0], end=List[1]))]
df['Month_Year'] = df['Date'].dt.strftime('%b-%Y')
df['Day'] = df['Date'].dt.strftime('%A')
df['Date'] = df['Date'].dt.strftime('%d-%b-%Y %A')
df = df[['Date']]
