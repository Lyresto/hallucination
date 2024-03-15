slopes = []

for col in df1.columns:
    if col != 'Time':
        df2 = df1[~np.isnan(df1[col])]
        df3 = df2[['Time', col]]
        npMatrix = np.matrix(df3)
        X, Y = npMatrix[:, 0], npMatrix[:, 1]
        slope = LinearRegression().fit(X, Y)
        m = slope.coef_[0]
        slopes.append(m)

slopes = np.array(slopes)
END SOLUTION
<code>
print(slopes)
