The issue with your code is that the constraint function `const` is defined inside the for loop, which leads to the incorrect behavior of the constraints. To fix this issue, you need to define the `const` function outside the loop. Here's the modified code:

```python
import numpy as np
from scipy.optimize import minimize

def function(x):
    return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3])

I = np.array((20, 50, 50, 80))
x0 = I

cons = []
steadystate = {'type': 'eq', 'fun': lambda x: x.sum() - I.sum()}
cons.append(steadystate)

def const(x, t):
    return x[t]

for t in range(4):
    cons.append({'type': 'ineq', 'fun': lambda x, t=t: const(x, t)})

out = minimize(function, x0, method="SLSQP", constraints=cons)
x = out["x"]

print(x)
```

Now the code will correctly enforce the non-negativity constraints on the decision variables.