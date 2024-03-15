fig, ax = plt.subplots()

ax.bar(df["celltype"], df["s1"], label="s1")
ax.bar(df["celltype"], df["s2"], bottom=df["s1"], label="s2")

ax.set_xlabel("celltype")
ax.set_ylabel("value")
ax.set_xticklabels(df["celltype"], rotation=45)

ax.legend()

plt.show()