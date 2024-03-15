# First, find the maximum length of any list in the 'codes' column
max_len = max(df['codes'].apply(len))

# Create a new dataframe with columns for each code index
new_df = pd.DataFrame(df['codes'].tolist(), columns=[f'code_{i}' for i in range(max_len)])

# Concatenate the new dataframe with the original dataframe
result = pd.concat([df, new_df], axis=1).drop('codes', axis=1)
