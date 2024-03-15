# One solution is to use a loop to iterate over the columns_check_list and build the condition step by step
condition = df1[columns_check_list[0]] == df2[columns_check_list[0]]
for column in columns_check_list[1:]:
    condition = condition & (df1[column] == df2[column])
result = list(condition)
