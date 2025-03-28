import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

X, y, X_test = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

X = np.array([735233.27082176, 735234.27082176, 735235.27082176, 735236.27082176,
              735237.27082176, 735238.27082176, 735239.27082176, 735240.27082176,
              735241.27082176, 735242.27082176, 735243.27082176, 735244.27082176,
              735245.27082176, 735246.27082176, 735247.27082176, 735248.27082176]).reshape(-1, 1)
y = np.array([0.00000000e+00, 1.36094276e+02, 4.46608221e+03, 8.72660888e+03,
              1.31375786e+04, 1.73580193e+04, 2.29420671e+04, 3.12216341e+04,
              4.11395711e+04, 5.07972062e+04, 6.14904935e+04, 7.34275322e+04,
              7.87333933e+04, 8.46302456e+04, 9.71074959e+04, 1.07146672e+05,
              1.17187952e+05, 1.26953374e+05, 1.37736003e+05, 1.47239359e+05,
              1.53943242e+05, 1.78806710e+05, 1.92657725e+05, 2.08912711e+05,
              2.22855152e+05, 2.34532982e+05, 2.41391255e+05, 2.48699216e+05,
              2.62421197e+05, 2.79544300e+05, 2.95550971e+05, 3.13524275e+05,
              3.23365158e+05, 3.24069067e+05, 3.24472999e+05, 3.24804951e+05]).reshape(-1, 1)

regressor = RandomForestRegressor(n_estimators=150, min_samples_split=1.0, random_state=42)
regressor.fit(X, y)

predict = regressor.predict(X)
print(predict)

### END SOLUTION
predict = regressor.predict(X_test)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(predict, f)
