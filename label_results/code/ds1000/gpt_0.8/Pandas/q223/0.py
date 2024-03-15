df['Column_x'] = df['Column_x'].fillna(0)  # Fill first 50% with 0
nan_count = df['Column_x'].isnull().sum()  # Count remaining NaN values
df['Column_x'] = df['Column_x'].fillna(1, limit=nan_count)  # Fill remaining NaN values with 1
