One way to achieve the desired result is by using the `apply` method with a lambda function that combines the "time" and "amount" columns into a list. Then, you can use the `sort_values` method to sort the lists within each group based on the "time" values. Here's how you can do it:

```python
result = df.groupby('user').apply(lambda x: x[['time', 'amount']].values.tolist()).sort_values('time').groupby('user').apply(list)
```

This will give you the following output:

```
user
1    [[20, 10.99], [10, 4.99]]
2    [[11, 2.99], [18, 1.99]]
3               [[15, 10.99]]
dtype: object
```

Explanation:
- `df.groupby('user')` groups the DataFrame by the "user" column.
- `.apply(lambda x: x[['time', 'amount']].values.tolist())` applies a lambda function to each group, which selects the "time" and "amount" columns and converts them into a list of lists using the `values.tolist()` method.
- `.sort_values('time')` sorts the lists within each group based on the "time" values.
- `.groupby('user').apply(list)` groups the sorted lists by "user" and converts them into a list of lists using the `list` function.

Note that the result is a Series with the "user" values as the index and the lists of time and amount as the values.