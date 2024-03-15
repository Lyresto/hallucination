# Use map to apply the values from the dict to the 'Member' column in the DataFrame
df['Date'] = df['Member'].map(dict)

# Use fillna to replace any NaN values with the original values in the 'Member' column
df['Date'] = df['Date'].fillna(df['Member'])

# Drop the 'Member' column since it's no longer needed
df = df.drop('Member', axis=1)

# Return the updated DataFrame
return df
### END SOLUTION