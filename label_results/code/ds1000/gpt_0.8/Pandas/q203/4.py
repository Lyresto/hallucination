To calculate the cumulative average for each row from end to head while ignoring zero values, you can use the following code:

<code>
df['Cumulative_Average'] = df.iloc[:, 1:].apply(lambda row: row[row != 0].mean(), axis=1)
df = df.fillna(0)
df = df.round(2)
