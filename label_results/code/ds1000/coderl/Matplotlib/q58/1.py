matplotlib.rcParams["xtick.direction"] = "vertical"

def plot(df, celltype="celltype"):
	s1 = df.sort_values("s1").groupby(celltype)
	s1.plot(kind="bar", x="s1", color="k")
	return s1.plot(kind="line", x="s1", color="r")

# Make the x-axis tick labels rotate 45 degrees.
# SOLUTION START
def rotate(ax):
	for ax in ax.patches:
		ax.get_xaxis().set_ticks_position("top")
		ax.get_yaxis().set_ticks_position("bottom")
		ax.get_yaxis().set_label_position("left")
		ax.get_xaxis().set_label_position("right")
		ax.set_ylabel("")

rotate(plt.gca())

plot(df, "celltype")
rotate(plt.gca())

# Make a stacked bar plot of s2 and s2. use celltype as the xlabel
# Make x-axis tick labels rotate 45 degrees.
# SOLUTION START
df = pd.DataFrame(
    {
	"celltype": ["foo", "bar", "qux", "woz"],
	"s1": [5, 9, 1, 7],
	"s2": [12, 90, 13, 87],
	"s3": [20, 30, 40, 50],
	"s4": [30, 40, 50, 60],
	"s5": [30, 40, 50, 60],
	"s6": [30, 40, 50, 60],
	"s7": [30, 40, 50, 60],
	"s8": [30, 40, 50, 60],
	"s9": [30, 40, 50, 60],
	"s10": [40, 50, 60, 50],
	"s11": [40, 50, 60, 50],
	"s12": [40, 50, 60, 50],
	"s13": [30, 40, 50, 60],
	"s14": [30, 40, 50