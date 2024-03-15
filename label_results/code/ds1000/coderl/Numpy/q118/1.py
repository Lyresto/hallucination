import numpy as np
def elementwise_function(element_1,element_2):
	return (element_1 + element_2)
def hcf(element_1,element_2):
	return element_1 * element_2

def partition(l, p):
	return [l[i] for i in range(p)]

def union(l1,l2):
	return [l1[i]+l2[i] for i in range(len(l1))]

x=[]
y=[]
z=[]
for i in range(len(x)):
	x.append([x[i][0]+x[i][1],x[i][0],x[i][2]])
for i in range(len(y)):
	y.append([y[i][0]+y[i][1],y[i][0],y[i][2]])
z=[]
for i in range(len(x)):
	for j in range(len(y)):
		z.append(elementwise_function(x[i][j],y[i][j]))
x=[]
y=[]
z=union(x,y)
for i in range(len(z)):
	for j in range(len(x)):
		x.append(z[i][j])
		y.append(hcf(z[i][j],x[j]))
print(x)
print(y)
