fig, ax = plt.subplots()
for i, j, k in zip(box_position, box_height, box_errors):
	ax.errorbar(i, j, yerr=k, c=c[i%4])
