import numpy as np
import scipy.stats
a,b=np.mean(a),np.mean(b)
c=np.array([sum(np.random.randn(i)) for i in range(40)]).T
d=np.array([sum(np.random.randn(i)) for i in range(50)]).T
p_value=scipy.stats.t.ppf(c,d)[2]
