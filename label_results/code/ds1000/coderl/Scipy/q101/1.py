from scipy.optimize import *
a=pd.DataFrame({'A1':[0,1,2,3,2,1,6,0,1,1,7,10]})
b=a.loc[10,:]
c=a.count()
weights=[]
for i in range(len(b)):
	weights.append((b[i]/c)[a.index==i])
m1=0.0
n=0.0
for i in range(len(weights)):
	m1=max(m1,max(weights[i]))
	n+=max(weights[i])
print(m1,n)
