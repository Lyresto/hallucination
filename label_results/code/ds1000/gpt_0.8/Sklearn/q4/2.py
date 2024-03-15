# Step 1: Convert the list in the 'Col3' column into separate columns
df_temp = df['Col3'].apply(pd.Series)

# Step 2: One-hot encode the separate columns using get_dummies function
df_encoded = pd.get_dummies(df_temp.apply(pd.Series).stack()).sum(level=0)

# Step 3: Concatenate the original DataFrame (df) with the encoded columns
df_out = pd.concat([df[['Col1', 'Col2']], df_encoded], axis=1)
END SOLUTION
<code>
df_out