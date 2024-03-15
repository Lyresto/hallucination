# First, select the rows whose value is bigger than the threshold
big_rows = df.loc[df['value'] >= thresh]

# If there are no big rows, return the original dataframe
if big_rows.empty:
    result = df
else:
    # Calculate the average of the big rows
    avg_value = big_rows['value'].mean()

    # Create a new row with the average value and a new label
    new_row = pd.DataFrame({'value': [avg_value]}, index=['X'])

    # Drop the big rows from the original dataframe
    df = df.drop(big_rows.index)

    # Concatenate the new row and the remaining rows
    result = pd.concat([df, new_row])
END SOLUTION
