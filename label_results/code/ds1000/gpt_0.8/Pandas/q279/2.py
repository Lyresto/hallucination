df = df[~((df.index.date == pd.to_datetime('2020-02-17').date()) | (df.index.date == pd.to_datetime('2020-02-18').date()))]
df['DayOfWeek'] = df.index.strftime('%d-%b-%Y %A')
