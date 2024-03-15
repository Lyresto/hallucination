#!/usr/bin/env python
from math import factorial as f
import numpy as np
from pandas import Series as A
a, b = [i for i in A.values()]
B = A.apply(lambda x: f(a)/(f(b)*f(a)), axis=1)
