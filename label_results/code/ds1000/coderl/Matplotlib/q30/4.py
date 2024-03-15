# # NOQA: E112
from itertools import zip_longest

def plot(df):
	p = df.pivot_table(y=0, x=1)
	return p.plot()

# def pivot(df):
#     index = 0
#     for i in range(0, 10):
#         df.loc[index, i] = df.loc[index, i-1] + 2 * df.loc[index, i]
#         index += 1

# plot(pivot(df))
# p1 = pivot(df)
# p2 = pivot(df, 'y')
# p3 = pivot(df, 'x')

# SOLUTION START
# import numpy as np
# from scipy import stats
#
# def plot(df):
#     res = stats.linregress(df.x, df.y)
#     x = res[0]
#     y = res[1]
#     plt.plot(x, y, 'ro')
#     return
#
# def pivot(df):
#     index = 0
#     for i in range(0, 10):
#         df.loc[index, i] = df.loc[index, i-1] + 2 * df.loc[index, i]
#         index += 1
#
# plot(pivot(df))
# p1 = pivot(df)
# p2 = pivot(df, 'y')
# p3 = pivot(df, 'x')

# SOLUTION START
# import numpy as np
# from scipy import stats
#
# def plot(df):
#     res = stats.linregress(df.x, df.y)
#     x = res[0]
#     y = res[1]
#     plt.plot(x, y, 'b-')
#     return
#
# def pivot(df):
#     index = 0
#     for i in range(0, 10):
#         df.loc[index, i] = df.loc[index, i-1] + 2 * df.loc[index, i]
#         index += 1
#
# plot(pivot(df))
# p1 = pivot