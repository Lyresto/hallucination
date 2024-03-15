One way to calculate the cumulative average for each row from end to head while ignoring zero values is by using the `apply` function in pandas.

Here's the solution:

```python
def calculate_cumulative_average(row):
    total = 0
    count = 0
    for value in reversed(row):
        if value != 0:
            total += value
            count += 1
        average = total / count if count != 0 else 0
        row = [average] + row[:-1]
    return row

df.iloc[:, 1:] = df.iloc[:, 1:].apply(calculate_cumulative_average, axis=1)
```

Explanation:
1. We define a helper function `calculate_cumulative_average` that takes a row as input.
2. We initialize two variables `total` and `count` to keep track of the sum and count of non-zero values, respectively.
3. We iterate through the row in reverse order using the `reversed` function.
4. If the value is not zero, we add it to the `total` and increment the `count`.
5. We calculate the average as `total / count` if `count` is not zero, otherwise set the average to zero.
6. We update the row by replacing the last element with the calculated average and shifting all other elements to the right.
7. Finally, we use the `apply` function along the rows (`axis=1`) of the DataFrame, excluding the first column, to apply the `calculate_cumulative_average` function to each row.

The resulting DataFrame `df` will have the cumulative average values for each row from end to head, ignoring zero values.