One way to filter the rows where the absolute value of all columns is less than 1 is to use the `apply()` function in combination with the `all()` function.

Here's the solution code:

```python
df = df[df.apply(lambda x: all(abs(x[col]) < 1 for col in df.columns if col.startswith('Value')), axis=1)]
```

This code applies a lambda function to each row (`axis=1`) of the dataframe. The lambda function checks if the absolute value of each column that starts with 'Value' is less than 1. The `all()` function returns True if all the conditions are True for a given row, and False otherwise.

By filtering the dataframe using this condition, you will get the desired result.