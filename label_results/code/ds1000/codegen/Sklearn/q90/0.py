df1 = load_data()
slopes =... # put solution in this variable
df1 = df1[~np.isnan(df1['A1'])]
df2 = df1[['Time','A1']]
npMatrix = np.matrix(df2)
X, Y = npMatrix[:,0], npMatrix[:,1]
slope = LinearRegression().fit(X,Y)
m = slope.coef_[0]
series= np.concatenate((SGR_trips, m), axis = 0)