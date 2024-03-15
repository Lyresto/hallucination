# First, we need to find the maximum length of the lists in the 'codes' column
max_length = df['codes'].apply(len).max()

# Next, we create a new DataFrame with columns code_0, code_1, ..., code_(max_length-1)
new_df = pd.DataFrame(df['codes'].tolist(), columns=[f'code_{i}' for i in range(max_length)])

# Finally, we concatenate the original DataFrame with the new DataFrame
result = pd.concat([df, new_df], axis=1)
result