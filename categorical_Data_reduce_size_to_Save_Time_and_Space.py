import pandas as pd
import sys

'''
One powerful Pandas feature is its Categorical dtype.

Even if you’re not always working with gigabytes of data in RAM, you’ve probably run into cases where straightforward operations on a large DataFrame seem to hang up for more than a few seconds.

Pandas object dtype is often a great candidate for conversion to category data. (object is a container for Python str, heterogeneous data types, or “other” types.) Strings occupy a significant amount of space in memory:

Categoricals are a pandas data type corresponding to categorical variables in statistics.


Currently, categorical data and the underlying Categorical is implemented as a Python object and not as a low-level NumPy array dtype. So NumPy itself doesn’t know about the new dtype:
'''

cities = pd.Series([
'Sanfrancisco',
'New York',
'New Delhi'
])

large_size = cities.apply(sys.getsizeof)
print(large_size)


'''
0    61
1    57
2    58
dtype: int64
'''

categorize_map = {v: k for k, v in enumerate(cities.unique())}

# encoding the object as an enumerated type (categorical variable).
as_categories = cities.map(categorize_map)

print(as_categories.apply(sys.getsizeof))

'''
0    24
1    28
2    28
dtype: int64
'''

'''
notice immediately that memory usage is just about cut in half compared to when the full strings are used with object dtype.

Note: I used sys.getsizeof() to show the memory occupied by each individual value in the Series. Keep in mind these are Python objects that have some overhead in the first place. (sys.getsizeof('') will return 49 bytes.)

There is also colors.memory_usage(), which sums up the memory usage and relies on the .nbytes attribute of the underlying NumPy array. Don’t get too bogged down in these details: what is important is relative memory usage that results from type conversion, as you’ll see next.
'''

# Another way to do this same thing is with Pandas’ pd.factorize(colors):
# pandas.factorize encodes input values as an enumerated type or categorical variable

print(pd.factorize(cities)[0])
# [0 1 2]

# https://realpython.com/python-pandas-tricks/#reader-comments