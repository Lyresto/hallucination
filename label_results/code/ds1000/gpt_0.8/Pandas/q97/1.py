To filter all rows where the absolute value of all columns (Value_A, Value_B, Value_C, etc.) is less than 1, you can use the `apply` method along with a lambda function to check the absolute value of each value in the row.

Here's how you can do it:

```python
import pandas as pd

df = pd.DataFrame({'A_Name': ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG'],
                   'B_Detail': ['X1', 'Y1', 'Z1', 'L1', 'M1', 'N1', 'K1'],
                   'Value_B': [1.2, 0.76, 0.7, 0.9, 1.3, 0.7, -2.4],
                   'Value_C': [0.5, -0.7, -1.3, -0.5, 1.8, -0.8, -1.9],
                   'Value_D': [-1.3, 0.8, 2.5, 0.4, -1.3, 0.9, 2.1]})

df = df[df.apply(lambda row: all(abs(row[col]) < 1 for col in df.columns if col.startswith('Value')), axis=1)]
```

This code applies a lambda function to each row of the DataFrame using the `apply` method. Inside the lambda function, it checks if the absolute value of each value in the row is less than 1 for columns that start with 'Value'. The `all` function checks if all the conditions are True for a given row, and `axis=1` ensures that the lambda function is applied row-wise.

The resulting filtered DataFrame is stored back in the `df` variable.