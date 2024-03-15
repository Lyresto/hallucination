import scipy.stats
a,b=scipy.stats.mean(a),scipy.stats.mean(b)
c=sum(a*b)/(len(a)+len(b))
