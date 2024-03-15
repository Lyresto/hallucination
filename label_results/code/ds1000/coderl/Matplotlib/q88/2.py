def second():
	while True:
		yield "second"

# the following lines are required to run the examples in the notebook:
# import numpy as np
# import pandas as pd
# x = np.arange(10)
# y = np.arange(10)
# fig, ax = plt.subplots(1, 1)
# ax.plot(y, x)
# # change the second x axis tick label to "second" but keep other labels in numerical
# # SOLUTION START
# df = pd.DataFrame({"a": x, "b": y})
# ax.plot(df["b"], df["a"])
# # keep the first line of the plot label for "second"
# ax.text(5, 5, "first")
# # Change the second x axis tick label to "second"
# ax.xaxis.set_major_locator(pd.MultipleLocator([second()]))
# # turn the x axis label to "second"
# ax.set_xticklabels(["second"])
# # turn the y axis label to "second"
# ax.set_yticklabels(["second"])
