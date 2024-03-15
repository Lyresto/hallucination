import numpy as np
from scipy.optimize import fsolve
eqn = lambda x, a, b: x + 2 * a - b**2
x0 = 0.5
root_list = fsolve(eqn, x0=x0, args=tuple([a,b]))
