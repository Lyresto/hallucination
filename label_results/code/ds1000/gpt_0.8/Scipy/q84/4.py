import scipy.integrate

def f(c, low, high):
    # create an empty array to store the solutions
    solutions = []
    
    # loop through each value of c
    for value in c:
        # define the function to be integrated
        def equation(x):
            return 2 * value * x
        
        # integrate the function
        result, error = scipy.integrate.quad(equation, low, high)
        
        # append the result to the solutions array
        solutions.append(result)
    
    # return the array of solutions
    return solutions

# example usage
c = [1, 2, 3]  # list of values for c
low = 0  # lower limit of integration
high = 1  # upper limit of integration

solution = f(c, low, high)
print(solution)