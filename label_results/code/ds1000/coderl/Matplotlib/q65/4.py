# SOLUTION END
# make two side-by-side subplots and in each subplot, plot y over x
# Title each subplot as "Y"
# SOLUTION START
# y = np.arange(10)
# x = np.arange(10)
# res = []
# for i, j in zip(y, x):
#     res.append(j)
#     res.append(i)
# df = pd.DataFrame({"Y": res})
# for i, j in zip(res, x):
#     df.loc[i,"Y"] = j
# df.plot(x, y)
# df.plot(y, x)
# pd.set_option('display.max_rows', None)
# pd.set_option('precision', None)
# pd.set_option('lines.linewidth', None)
# pd.set_option('width', None)
# pd.set_option('show_grid', None)
# pd.set_option('grid.color', None)
# pd.set_option('vertical_spines', None)
# pd.set_option('legend.fontsize', None)
# pd.set_option('grid.linewidth', None)
# pd.set_option('axis.labelsize', None)
# pd.set_option('grid.color', None)
# pd.set_option('spines.labelsize', None)
# SOLUTION END
# make x-axis
# res = []
# for i, j in zip(y, x):
#     res.append(j)
#     res.append(i)
# df = pd.DataFrame({"Y": res})
# df.plot(x, y)
# pd.set_option('display.max_rows', None)
# pd.set_option('precision', None)
# pd.set_option('lines.linewidth', None)
# pd.set_option('width', None)
# pd.set_option('show_grid', None)
# pd.set_option('grid.color', None)
# pd.set_option('vertical_spines', None)
# pd.set_option('legend.fontsize', None)
#