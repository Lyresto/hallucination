import numpy as np
a,b = np.array(map(int,input().split()),'i')
c = np.array(list(filter(lambda x:(x in range(1,8)and a[x] in b),a))
print(c)
