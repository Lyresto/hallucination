def myplot(x,y):
	p1 = pd.Series(y)
	p1.plot(x, x)
	p1.plot(x,y,color="r")
	p1.set_title("My Title")
	return p1

p1 = myplot(x,y)

# SAVE AND DROP FROM THE PAGE
# (see http://www.codewars.com/kata/5057367.html)

# SOLUTION END
