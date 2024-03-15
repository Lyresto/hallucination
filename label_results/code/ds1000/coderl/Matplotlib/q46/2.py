sns.distplot(x, y, kind="hex", color="k")
sns.distplot(x, y, kind="kde", color="y")

plt.xlabel("x")
plt.ylabel("y")

sns.despine(left=True)
