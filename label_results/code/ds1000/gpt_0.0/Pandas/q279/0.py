# Solution for deleting particular days
dates_to_delete = ['2020-02-17', '2020-02-18']
for date in dates_to_delete:
    df = df[df.index.date != pd.to_datetime(date).date()]

# Solution for converting date to desired format
df['DayOfWeek'] = df.index.strftime('%d-%b-%Y %A')
df = df[['DayOfWeek'] + list(df.columns[:-1])]
END SOLUTION