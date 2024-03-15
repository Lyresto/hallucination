# First, we need to find the index of the last occurrence of each duplicate
last_occurrence = df.duplicated(subset=['col1','col2'], keep='last')

# Then, we can use the groupby method to get the index of the last occurrence for each group of duplicates
last_index = df[last_occurrence].groupby(['col1','col2']).tail(1).index

# Finally, we can create a new column in the duplicate dataframe with the index of the last occurrence
duplicate = df[last_occurrence].copy()
duplicate['index_original'] = last_index
