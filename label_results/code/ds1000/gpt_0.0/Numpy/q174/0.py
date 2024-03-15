# Flatten the arrays and create a dictionary
data_dict = {'lat': lat.flatten(), 'lon': lon.flatten(), 'val': val.flatten()}

# Create the dataframe
df = pd.DataFrame(data_dict)

# Return the dataframe
return df
### END SOLUTION