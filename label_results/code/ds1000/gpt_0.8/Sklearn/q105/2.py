train_size = 0.8
split_index = int(len(features_dataframe) * train_size)
train_dataframe = features_dataframe.iloc[split_index:]
test_dataframe = features_dataframe.iloc[:split_index]
