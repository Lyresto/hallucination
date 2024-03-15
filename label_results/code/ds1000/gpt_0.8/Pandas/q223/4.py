percent_fill = int(len(df['Column_x'])/2) # calculate the number of NaN values to fill with each value

df['Column_x'].fillna(0, limit=percent_fill, inplace=True) # fill first half with 0
df['Column_x'].fillna(1, inplace=True) # fill remaining NaN values with 1
