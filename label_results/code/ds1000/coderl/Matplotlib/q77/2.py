def main():
	df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'a': a})
	sub1 = df['y'].plot(figsize=(6, 6))
	sub2 = df['z'].plot(figsize=(6, 6))
	#sub1.set_title('Y and Z')
	#sub2.set_title('Z and Y')
	return sub1 + sub2

# SOLUTION END
sub1 = main()
sub2 = main()

#sub1.savefig('test.png', dpi=300)
sub2.savefig('test.png', dpi=300)

# SOLUTION START
#sub1.show()
#sub2.show()
