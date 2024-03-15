fig = plt.figure()

# subplot 1
ax1 = fig.add_subplot(211)
ax1.plot(time, Swdown, "-", label="Swdown")
ax1.plot(time, Rn, "-", label="Rn")
ax1.legend(loc=0)
ax1.grid()
ax1.set_xlabel("Time (h)")
ax1.set_ylabel(r"Radiation ($MJ\,m^{-2}\,d^{-1}$)")
ax1.set_ylim(-20, 100)

# subplot 2
ax2 = fig.add_subplot(212)
ax2.plot(time, temp, "-r", label="temp")
ax2.legend(loc=0)
ax2.grid()
ax2.set_xlabel("Time (h)")
ax2.set_ylabel(r"Temperature ($^\circ$C)")
ax2.set_ylim(0, 35)

plt.tight_layout()
plt.show()
plt.clf()