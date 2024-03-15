# Define a function to extract key-value pairs from the message column
def extract_key_value_pairs(message):
    # Remove brackets and split by comma
    pairs = message.strip('[]').split(', ')
    # Split each pair by colon and create a dictionary
    pairs_dict = {pair.split(': ')[0]: pair.split(': ')[1] for pair in pairs}
    return pairs_dict

# Apply the function to the message column and expand the resulting dictionary into columns
df = pd.concat([df, df['message'].apply(extract_key_value_pairs).apply(pd.Series)], axis=1)

# Drop the original message column
df.drop('message', axis=1, inplace=True)

# Replace empty strings with 'none'
df.replace('', 'none', inplace=True)

# Reorder columns
df = df[['name', 'status', 'number', 'job', 'money', 'wife', 'group', 'kids']]
