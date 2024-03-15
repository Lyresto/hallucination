#iterate through columns
for Col in range(sa.shape[1]):
    Column = sa[:,Col].data
    List = [x**2 for x in Column]
    #get the column length
    Len = math.sqrt(sum(List))
    #normalize column
    sa[:,Col] = (1/Len)*Column
END SOLUTION
