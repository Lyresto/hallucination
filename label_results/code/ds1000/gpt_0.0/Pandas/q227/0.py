# One way to solve this is to use the zip function to combine the dataframes and then apply the tuple function to each row

dfs = [a, b, c] # list of dataframes
zipped = zip(*dfs) # combine the dataframes
result = pd.DataFrame([tuple(row) for row in zipped], columns=a.columns) # apply tuple function to each row and create dataframe
