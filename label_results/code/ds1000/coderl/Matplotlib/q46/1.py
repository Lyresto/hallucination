sns.lineplot(x, y, color="r", line_kw={"color": "k"})
sns.lineplot(y, x, color="b", line_kw={"color": "g"})
sns.lineplot(x, y, line_kw={"color": "m"}, y_lw=2, legend=True)
