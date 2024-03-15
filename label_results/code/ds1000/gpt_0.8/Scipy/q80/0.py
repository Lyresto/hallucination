for t in range (4):
    def const(x, t=t):    
        y=x[t]
        return y
    cons.append({'type':'ineq', 'fun': const})
