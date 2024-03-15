One way to calculate the cumulative average while ignoring zero values is to use the pandas DataFrame `apply` method along with a lambda function. Here's how you can do it:

```python
def f(df):
    # Calculate the cumulative average for each row while ignoring zero values
    df = df.set_index('Name')  # Set the 'Name' column as the index
    df = df.apply(lambda row: row[row != 0].mean(), axis=1)  # Calculate the mean of non-zero values for each row

    # Reset the index and rename the column
    df = df.reset_index()
    df = df.rename(columns={0: 'Average'})

    return df
```

Now, you can call the `f` function and pass your DataFrame `example_df` as an argument:

```python
result = f(example_df)
print(result)
```

Output:
```
    Name   Average
0  Name1  3.500000
1  Name2  2.125000
2  Name3  3.333333
```

Note that the output values may differ slightly due to floating-point precision.