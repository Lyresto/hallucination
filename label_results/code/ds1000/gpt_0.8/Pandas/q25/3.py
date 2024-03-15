# Filter data between the given dates
mask = (df['Date'] >= List[0]) & (df['Date'] <= List[1])
filtered_df = df.loc[mask]

# Format the date column
filtered_df['Date'] = filtered_df['Date'].dt.strftime('%d-%b-%Y %A')

# Rename the column
filtered_df = filtered_df.rename(columns={'Date': 'Formatted Date'})

# Reset index
filtered_df = filtered_df.reset_index(drop=True)

# Final output
df = filtered_df[['Formatted Date']]
