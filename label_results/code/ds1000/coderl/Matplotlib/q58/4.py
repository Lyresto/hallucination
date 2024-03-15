def plot(df, celltype):
	d = {
		"foo": 0,
		"bar": 1,
		"qux": 2,
		"woz": 3,
	}
	# df = df.reset_index()
	
	for i, s in enumerate(df["s1"]):
		print(s, df["celltype"][i])
		d[df["celltype"][i]] += 1
	
	print(d)
	
	matplotlib.pyplot.bar(
		df["s1"],
		df["s1"],
		celltype,
		height=0.35,
		width=0.35,
	)
	# matplotlib.pyplot.xticks(df["s1"], df["celltype"])
	# matplotlib.pyplot.yticks(df["s1"], df["celltype"])
	matplotlib.pyplot.xticks(
		range(len(df["celltype"])),
		df["celltype"],
		rotation=45,
	)
	matplotlib.pyplot.yticks(range(len(df["celltype"])), df["celltype"])
	
	return

plot(df, "foo")

# make a scatter plot of s1 and s1
# use celltype as the xlabel
# Make x-axis tick labels rotate 45 degrees
# SOLUTION START
