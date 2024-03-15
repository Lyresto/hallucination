g = sns.FacetGrid(df, row="b", height=2, aspect=3)
g.map(sns.pointplot, "a", "c")

for ax in g.axes.flat:
    ax.set_xticks(np.arange(1, 31, 2))

plt.show()