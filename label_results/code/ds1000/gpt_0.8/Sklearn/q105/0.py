train_size = 0.8
train_index = int(len(features_dataframe) * train_size)
train_dataframe = features_dataframe[:train_index]
test_dataframe = features_dataframe[train_index:]
