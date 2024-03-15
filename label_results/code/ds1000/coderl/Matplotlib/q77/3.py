# SOLUTION END
df1 = pd.DataFrame({"x": x, "y": y, "z": z, "a": a})
df2 = pd.DataFrame({"x": x, "y": y, "z": z, "a": a})

fig1 = fig1.add_subplot(2, 1, 1)
df1.plot(y='x', x='y', ax=fig1)
df1.plot(z='x', x='z', ax=fig1)
df1.plot(a='y', x='z', ax=fig1)

fig2 = fig2.add_subplot(2, 1, 2)
df2.plot(x='y', y='z', z='a', ax=fig2)
df2.plot(a='y', y='z', z='a', ax=fig2)

# show plot
#plt.show()
