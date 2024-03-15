#csr sparse matrix
self.__WeightMatrix__ = self.__WeightMatrix__.tocsr()
#iterate through columns
for Col in range(self.__WeightMatrix__.shape[1]):
   Column = self.__WeightMatrix__[:,Col].data
   List = [x**2 for x in Column]
   #get the column length
   Len = math.sqrt(sum(List))
   #normalize column
   self.__WeightMatrix__[:,Col] = (1/Len) * Column
END SOLUTION