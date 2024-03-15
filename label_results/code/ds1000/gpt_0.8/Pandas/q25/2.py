# filter the dataframe to only include dates between the two dates in the list
df = df[(df['Date'] >= List[0]) & (df['Date'] <= List[1])]

# create a new column with the desired format
df['Formatted Date'] = df['Date'].dt.strftime('%d-%b-%Y %A')

# select only the 'Formatted Date' column
df = df[['Formatted Date']]
