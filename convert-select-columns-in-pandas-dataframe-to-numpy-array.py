import pandas as pd

a = pd.DataFrame([[4, 5], [12,31]])
print(a)

a_array = a.iloc[:, 0].values
print(a_array)