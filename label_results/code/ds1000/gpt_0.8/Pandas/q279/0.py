# Delete particular days
delete_dates = ['2020-02-17', '2020-02-18']
df = df[~df.index.date.isin(delete_dates)]
