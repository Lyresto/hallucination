import numpy as np
import pandas as pd
import io
from scipy import integrate
import scipy.optimize


def test(result, ans):
    np.testing.assert_allclose(result, ans)
    return 1
