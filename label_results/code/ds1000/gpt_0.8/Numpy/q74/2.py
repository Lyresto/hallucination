def f(a, pos, element):
    return np.insert(a, pos, element)

# Test the function
a = np.asarray([1,2,3,4])
a = f(a, pos=2, element=66)
print(a)