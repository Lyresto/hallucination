g = sns.FacetGrid(df, row="b", height=4, aspect=1.5)
g.map(sns.pointplot, "a", "c")

# Set the xticks interval to 1
plt.xticks(np.arange(0, 31, 2))

# Show the plot
plt.show()
