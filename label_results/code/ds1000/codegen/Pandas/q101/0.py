import pandas as pd


df = pd.DataFrame({'A': ['Good &LT bad', 'BB', 'CC', 'DD', 'Good &LT; bad'], 'B': range(5), 'C': ['Good &LT; bad'] * 5})
