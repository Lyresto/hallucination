check = np.where(~df1[columns_check_list].eq(df2[columns_check_list]).any(axis=1), True, False)
