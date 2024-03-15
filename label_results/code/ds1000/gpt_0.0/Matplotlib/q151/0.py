g = sns.FacetGrid(df, row="b", height=1.5, aspect=4)
g.map(sns.pointplot, "a", "c", order=np.arange(1, 31), color="red")
g.set(xticks=np.arange(1, 31, 2), xticklabels=np.arange(1, 31, 2))
plt.show()
