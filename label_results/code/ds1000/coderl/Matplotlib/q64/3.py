# SOME CODE HERE
from random import randint

x = [randint(-10, 10) for i in range(2)]
y = [randint(-10, 10) for i in range(2)]
z = [randint(-10, 10) for i in range(2)]
# SOLUTION END


# this doesn't work - needs to be adjusted!

fig = plt.figure()
ax = fig.add_subplot(111)
sw = ax.plot(x, y, "-", label="y")
cn = ax.twinx()
tb = cn.plot(x, z, "-r", label="z")
cn.legend(loc=0)
cn.grid()
cn.set_xlabel("Time (h)")
cn.set_ylabel(r"Radiation ($MJ\,m^{-2}\,d^{-1}$)")
cn.set_ylim(0, 35)
