# First, we need to reset the index so that the 'time' index becomes a regular column
df = df.reset_index()

# Then, we can sort the DataFrame by 'VIM' and 'time' using pandas.DataFrame.sort_values
result = df.sort_values(['VIM', 'time'])

# Finally, we can set the MultiIndex back using pandas.DataFrame.set_index
result = result.set_index(['treatment', 'dose', 'time'])
