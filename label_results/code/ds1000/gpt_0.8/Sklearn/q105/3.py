# Calculate the index at which to split the data
split_index = int(len(features_dataframe) * train_size)

# Split the data into train and test sets
train_dataframe = features_dataframe[split_index:]
test_dataframe = features_dataframe[:split_index]
