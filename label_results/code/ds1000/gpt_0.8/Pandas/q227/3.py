One way to achieve this is by using the `zip` function along with a list comprehension. Here's how you can do it:

```python
result = pd.DataFrame([tuple(zip(*df_list)) for df_list in zip(a.values, b.values, c.values)], columns=a.columns)
```

This code first uses the `zip` function to iterate over the rows of the three dataframes simultaneously. Then, using a list comprehension, it applies the `zip` function again to transpose the values of each row, resulting in tuples. Finally, it constructs a new dataframe using the list of tuples and the column names from dataframe `a`.

The resulting dataframe `result` will have the desired structure:

```
      one         two
0  (1, 5, 9)  (2, 6, 10)
1  (3, 7, 11) (4, 8, 12)
```

This solution can handle an arbitrary number of dataframes, as long as they have the same number of rows and columns.