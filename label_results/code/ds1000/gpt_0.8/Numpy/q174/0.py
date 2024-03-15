import pandas as pd

# Create a pandas DataFrame with columns 'lat', 'lon', 'val'
df = pd.DataFrame({'lat': lat.flatten(), 'lon': lon.flatten(), 'val': val.flatten()})

# Sort the DataFrame by the order of the original arrays
df = df.sort_index()

# Reset the index of the DataFrame
df = df.reset_index(drop=True)

# Return the resulting DataFrame
return df