# extract key-value pairs from message column
key_values = df['message'].str.extractall(r'(\w+):\s*([^,\]]+)')[1]

# pivot key-value pairs into separate columns
pivoted = key_values.reset_index().pivot(index='level_0', columns=0, values=1)

# join pivoted data with original dataframe
result = pd.concat([df.drop('message', axis=1), pivoted], axis=1)
result.fillna('none', inplace=True)
