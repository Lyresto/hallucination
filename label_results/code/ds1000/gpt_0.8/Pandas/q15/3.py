# define a function to extract the key-value pairs from the message column
def extract_key_value_pairs(message):
    # remove the brackets and split on commas
    pairs = message.strip('[]').split(',')
    # split each pair on the colon to get key and value
    pairs = [pair.split(':') for pair in pairs]
    # strip whitespace from keys and values
    pairs = [[kv.strip() for kv in pair] for pair in pairs]
    # return as a dictionary
    return dict(pairs)

# apply the function to the message column to create a new column with the key-value pairs
df['key_value_pairs'] = df['message'].apply(extract_key_value_pairs)

# create a new dataframe with the expanded key-value pairs
expanded_df = pd.json_normalize(df['key_value_pairs'])

# join the expanded dataframe back to the original dataframe
result = pd.concat([df[['name', 'status', 'number']], expanded_df], axis=1)

# replace empty strings with 'none'
result = result.replace('', 'none')
