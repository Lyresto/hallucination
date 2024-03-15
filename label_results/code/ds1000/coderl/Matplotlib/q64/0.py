# https://www.codechef.com/plots/3d_plot.html
# SOLUTION END

# make a new figure
fig = plt.figure()
ax = fig.add_subplot(111)
swdown = np.random.random(10) * 100 - 10
rn = np.random.random(10) * 100 - 10
temp = np.random.random(10) * 30

# plot the data
ax.plot(time, swdown, '-', label="Swdown")
ax.plot(time, rn, '-', label="Rn")
ax2 = ax.twinx()
ax2.plot(time, temp, '-r', label="temp")
ax.legend(loc=0)
ax.grid()
ax.set_xlabel("Time (h)")
ax.set_ylabel(r"Radiation ($MJ\,m^{-2}\,d^{-1}$)")
ax2.set_ylabel(r"Temperature ($^\circ$C)")
ax2.set_ylim(0, 35)

# show the plots
plt.show()
