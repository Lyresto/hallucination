# Solution

To split the data in a way that the test set is older than the train set, you can follow these steps:

1. Determine the index at which the split should occur based on the percentage of data to be used for training.
2. Split the data into two parts using the determined index.
3. Assign the first part to the test set and the second part to the train set.

Here is an example of how you can implement this using pandas:

```python
# Step 1: Determine the index at which the split should occur
split_index = int(len(features_dataframe) * train_size)

# Step 2: Split the data into two parts
train_data = features_dataframe[:split_index]
test_data = features_dataframe[split_index:]

# Step 3: Assign the data to the train and test sets
train_dataframe = train_data.sort_values("date")
test_dataframe = test_data.sort_values("date")
```

Note: In the above code, I used the `sort_values()` function instead of `sort()` to sort the data by date. The `sort()` function is deprecated in newer versions of pandas.

This code will split the data such that 80% of the data is used for training and 20% is used for testing, and the test set will be older than the train set.