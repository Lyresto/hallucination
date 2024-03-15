import scipy.integrate

def solve_integral(c_values):
    # create an empty array to store the results
    results = []
    
    # loop through each value of c
    for c in c_values:
        # define the function to be integrated
        def f(x):
            return 2*c*x
        
        # solve the definite integral
        result, error = scipy.integrate.quad(f, 0, 1)
        
        # append the result to the results array
        results.append(result)
    
    return results

# example usage
c_values = [1, 2, 3, 4, 5]
solution = solve_integral(c_values)
print(solution)