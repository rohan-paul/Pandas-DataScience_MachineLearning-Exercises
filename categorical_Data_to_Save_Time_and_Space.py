import pandas as pd
import sys

colors = pd.Series([
'periwinkle',
'mint green',
'burnt orange'
])

size = colors.apply(sys.getsizeof)

print(size)

mapper = {v: k for k, v in enumerate(colors.unique())}
as_int = colors.map(mapper)
print(as_int.apply(sys.getsizeof))



# cat_var =  pd.factorize(colors)
# print(cat_var)