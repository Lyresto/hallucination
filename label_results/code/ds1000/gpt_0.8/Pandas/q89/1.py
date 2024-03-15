result = [(df1[column] != df2[column]).any() for column in columns_check_list]
