# Find the index to split the data into train and test sets
split_index = int(len(features_dataframe) * 0.8)

# Split the data into train and test sets
train_dataframe = features_dataframe.iloc[:split_index]
test_dataframe = features_dataframe.iloc[split_index:]

# Make sure the test set is older than the train set
if test_dataframe.iloc[0]["date"] < train_dataframe.iloc[-1]["date"]:
    train_dataframe = pd.concat([train_dataframe, test_dataframe.iloc[:-1]])
    test_dataframe = test_dataframe.iloc[-1:]

# Sort the dataframes by date
train_dataframe = train_dataframe.sort_values(by=["date"])
test_dataframe = test_dataframe.sort_values(by=["date"])
