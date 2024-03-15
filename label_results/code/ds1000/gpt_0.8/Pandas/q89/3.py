check = np.where(df1[columns_check_list] != df2[columns_check_list])

result = [False] * len(columns_check_list)
for i in check[1]:
    result[i] = True
