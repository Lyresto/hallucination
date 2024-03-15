from itertools import zip_longest

# SOLUTION END

ax = pd.Series(y, index=x)
ax.plot.box()

# SOLUTION START
# x_values = [i for i, _ in enumerate(ax.values) if i % 2 == 0]
# y_values = [j for _, j in zip_longest(*zip_longest(ax.values, x_values), fillvalue=0)]
# fig, ax = plt.subplots()
# ax.plot(x_values, y_values)
# ax.set_ylabel('Y')
# ax.set_xticks(x_values)
# ax.set_xticklabels(x_values)
# SAVE AND MOVE IT
#plt.savefig("test.png")
