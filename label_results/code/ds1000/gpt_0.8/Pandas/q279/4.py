# Deleting specific dates

To delete specific dates from the 'Date' column, you can use the `~` operator to invert the condition and select the rows that do not match the given dates.

Here is an example of how you can delete '2020-02-17' and '2020-02-18' from the 'Date' column:

```
dates_to_delete = ['2020-02-17', '2020-02-18']
sp = sp[~sp.index.date.isin(pd.to_datetime(dates_to_delete))]
```

This will filter out the rows with dates '2020-02-17' and '2020-02-18' from the dataframe.

# Formatting dates

To format the dates as '15-Dec-2017 Friday', you can use the `strftime` function to convert the date to the desired format.

Here is an example of how you can format the dates in the 'Date' column:

```
sp.index = sp.index.strftime('%d-%b-%Y %A')
```

This will convert the dates in the 'Date' column to the format '15-Dec-2017 Friday'.