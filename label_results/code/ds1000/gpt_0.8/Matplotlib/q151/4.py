g = sns.FacetGrid(df, row="b", height=2, aspect=3)
g.map(sns.pointplot, "a", "c")
g.set(xticks=np.arange(0, 31, 2))
plt.show()