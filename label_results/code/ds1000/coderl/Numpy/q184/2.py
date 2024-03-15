# def linear_interpolate(arr, x, y, k):
#     i = 0
#     for i in range(k):
#         for j in range(k):
#             x1 = x[i]
#             y1 = y[j]
#             val = arr[i][j] * (y1 - y[j]) + arr[i][j] * (x1 - x[j])
#     return val

from scipy.interpolate import interp2d

def linear_interpolate(arr, x, y, k):
	i = 0
	for i in range(k):
		for j in range(k):
			x1 = x[i]
			y1 = y[j]
			val = interp2d(arr, [x1, y1], kind='linear')
			arr[i][j] = val(i, j)
	return arr
