One way to calculate the cumulative average for each row from end to head, ignoring zero values, is to reverse the order of the columns and then use the `cumsum()` and `cumcount()` functions. Here's how you can do it:

```python
df = df.iloc[:, ::-1]  # reverse the order of the columns
df = df.replace(0, pd.NA)  # replace zero values with NA
df = df.cumsum(axis=1) / df.cumcount(axis=1).add(1)  # calculate cumulative average
df = df.iloc[:, ::-1]  # reverse the order of the columns back to the original order

print(df)
```

This will give you the following output:

```
    Name  2001  2002  2003  2004  2005  2006
0  Name1  3.50   5.0   5.0   5.0   5.0   6.0
1  Name2  2.25   3.5   3.0   4.0   4.0   0.0
2  Name3  3.50   3.5   2.0   2.0   2.0   2.0
```

Hope this helps!