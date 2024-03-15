
    new_a = a.copy()
    new_a[:,0] = a[:,0] - a[:,1]
    new_a[:,1] = a[:,0]
    return new_a
    ### END SOLUTION

def load_data():
    #