def plot_cutoff():
	x = [3, 4, 5, 6]
	cutoff, = plt.plot(x, 'cutoff', color='orange')
	plt.xlabel('Cutoff')
	plt.ylabel('Normalized Cutoff')
	#plt.yticks(range(3), ['cutoff', 'normalized cutoff'], rotation=45)
	plt.grid(True)
	
	return cutoff

cutoff = plot_cutoff()
