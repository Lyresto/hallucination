# SOLUTION START
x_label = "X"
y_label = "Y"

df = pd.DataFrame({x_label: x, y_label: y})

# Make x and y labels red
df.loc[:,'x'].plot(ax=plt.gca(),x='X',y='Y')

# Make x and y labels blue
df.loc[:,'y'].plot(ax=plt.gca(),x='X',y='Y',color='blue')

# Make x and y labels green
df.loc[:,'x'].plot(ax=plt.gca(),x='Y',y='X',color='green')

# Make x and y labels cyan
df.loc[:,'y'].plot(ax=plt.gca(),x='X',y='Y',color='cyan')

# Make x and y labels blue grey
df.loc[:,'x'].plot(ax=plt.gca(),x='Y',y='X',color='greatblue')

# Make x and y labels cyan grey
df.loc[:,'y'].plot(ax=plt.gca(),x='Y',y='X',color='cyan')

# Make x and y labels green grey
df.loc[:,'x'].plot(ax=plt.gca(),x='Y',y='X',color='green')

# Make x and y labels blue grey
df.loc[:,'y'].plot(ax=plt.gca(),x='Y',y='X',color='yellow')

# Make x and y labels cyan grey
df.loc[:,'x'].plot(ax=plt.gca(),x='Y',y='X',color='greatblue')

# Make x and y labels blue grey
df.loc[:,'y'].plot(ax=plt.gca(),x='Y',y='X',color='cyan')

# Make x and y labels green grey
df.loc[:,'x'].plot(ax=plt.gca(),x='Y',y='X',color='green')

# Make x and y labels blue grey
df.loc[:,'y'].plot(ax=plt.gca(),x='X',y='Y',color='