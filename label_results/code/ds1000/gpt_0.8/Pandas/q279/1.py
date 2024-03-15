df = df[~df.index.date.isin([pd.to_datetime('2020-02-17').date(), pd.to_datetime('2020-02-18').date()])]
df['DayOfWeek'] = df.index.strftime('%d-%b-%Y %A')
