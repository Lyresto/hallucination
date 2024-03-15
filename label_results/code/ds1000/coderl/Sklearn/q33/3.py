from heapq import heappush, heappop, heapify
from math import sqrt
def regressor(X,Y):
	lis = []
	for i in range(len(X)):
		heappush(lis, (X[i],i))
	for i in range(len(X)):
		X[i] = heappop(lis)[1]
	for i in range(len(X)):
		Y[i] = regressor(X,Y)[1]
	return regressor(X,Y)
