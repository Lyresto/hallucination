def df_xy(x,y):
	return [(i,j) for i in range(1,len(df.b)+1) for j in range(len(df.c)) if i <= x <= j]

def f():
	df1 = pandas.DataFrame(df)
	sns.pointplot(df1,"b",x="a")
	sns.pointplot(df1,"c",y="a")
	# SAVE AND PLOT WITH INLINE PATTERN
	plt.show()

df_xy(1,0)
df_xy(2,1)
