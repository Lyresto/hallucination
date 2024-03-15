matplotlib.rcParams["xtick.labelsize"] = 8

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)

for i in range(len(df)):
	ax.bar(df["s1"], df["s1"], width=1.2, align="center")
	ax.set_xticks(df["celltype"])
	ax.set_xticklabels(df["celltype"])

ax.xaxis.set_ticklabels(("foo", "bar", "qux", "woz"))

# Make the x-axis tick labels rotate 45 degrees.
#SOLUTION END
