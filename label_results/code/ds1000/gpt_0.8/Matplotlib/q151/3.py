g = sns.FacetGrid(df, row="b", height=2.5, aspect=3)
g.map(sns.pointplot, "a", "c", palette="dark", ci=None)
g.set(xticks=np.arange(0, 31, 2), xticklabels=np.arange(0, 31, 2))
plt.show()