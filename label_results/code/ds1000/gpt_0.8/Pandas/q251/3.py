# Get the maximum length of the lists in 'codes'
max_len = df['codes'].apply(len).max()

# Create new columns with 'code_' prefix
new_columns = [f'code_{i}' for i in range(max_len)]

# Split the lists in 'codes' into separate columns
df[new_columns] = pd.DataFrame(df['codes'].tolist())

result = df
