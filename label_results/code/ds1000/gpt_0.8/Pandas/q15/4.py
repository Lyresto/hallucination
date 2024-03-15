# Function to extract key value pairs from message column
def extract_key_value_pairs(row):
    message = row['message'].strip('[]')
    pairs = message.split(', ')
    key_values = {}
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(': ')
            key_values[key.strip()] = value.strip()
    return key_values

# Apply function to create new columns
df = pd.concat([df, pd.DataFrame(df.apply(extract_key_value_pairs, axis=1).tolist())], axis=1)

# Drop original message column
df = df.drop(columns=['message'])

# Replace missing values with 'none'
df = df.fillna('none')

result = df
