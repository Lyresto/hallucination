# Define a function to extract the key-value pairs from the message column
def extract_info(row):
    info = {}
    # Remove brackets and split by commas
    items = row['message'][1:-1].split(',')
    for item in items:
        # Split each item by colon to get key-value pairs
        key, value = item.split(':')
        # Strip whitespace from keys and values
        key = key.strip()
        value = value.strip()
        # Add key-value pair to dictionary
        info[key] = value
    return info

# Apply the function to each row to create a new column with the extracted info
df['info'] = df.apply(extract_info, axis=1)

# Use the apply method again to expand the info column into separate columns
df = pd.concat([df.drop('info', axis=1), df['info'].apply(pd.Series)], axis=1)

# Replace empty values with 'none'
df = df.fillna('none')

# Reorder columns
df = df[['name', 'status', 'number', 'job', 'money', 'wife', 'group', 'kids']]

result = df
