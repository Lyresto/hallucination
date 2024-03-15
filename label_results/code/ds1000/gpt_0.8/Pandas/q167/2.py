One way to solve this problem is to use the `groupby` function to group the data frame by the values in column 'b'. Then, we can apply the `mean` and `std` functions to each group to calculate the mean and standard deviation of column 'a' within each group. Finally, we can combine these results into a new data frame.

Here is the solution:
```python
result = df.groupby('b')['a'].agg(['mean', 'std'])
```
The `groupby('b')` function groups the data frame by the unique values in column 'b'. Then, we select column 'a' with `['a']`. The `agg(['mean', 'std'])` function calculates the mean and standard deviation for each group.

The resulting data frame will have the mean and standard deviation as separate columns, with the group values as the index.

Output:
```
   mean        std
b                 
1  16.0   6.082763
2  23.0   1.000000
3  40.0  13.228757
```