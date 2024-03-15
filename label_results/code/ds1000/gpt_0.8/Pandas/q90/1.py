check = df1[columns_check_list] == df2[columns_check_list]
result = check.all(axis=0).tolist()
