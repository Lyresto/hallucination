One way to aggregate user transactions into lists in pandas, while sorting the time and amount in the same order, is to use the `apply` method with a lambda function that returns a list of tuples for each user. Here is the solution:

```python
df.groupby('user').apply(lambda x: x[['time', 'amount']].apply(tuple, axis=1).tolist())
```

This will give you the desired output:

```
user
1    [(20, 10.99), (10, 4.99)]
2    [(11, 2.99), (18, 1.99)]
3               [(15, 10.99)]
dtype: object
```

In this solution, we select the 'time' and 'amount' columns using `x[['time', 'amount']]`, then apply the `tuple` function to each row using `apply(tuple, axis=1)`. Finally, we convert the resulting DataFrame into a list using `tolist()`.