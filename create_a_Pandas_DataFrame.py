import numpy as np
import pandas as pd

''' DataFrame can be called as a bunch of series objects put together to share same index. DataFrames are 2D array with Series as their columns. It can be created using pd.DataFrame() with various inputs such as lists, dictionary, ndarray, other files (.csv, .xml, .sas etc).

Example of converting other data structures, such as lists or NumPy arrays, to Pandas DataFrames. '''

data = np.array([['', 'Col1', 'Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])

print(pd.DataFrame(data=data[1:, 1:],
                   index=data[1:, 0],
                   columns=data[0, 1:]
))

'''
     Col1 Col2
Row1    1    2
Row2    3    4
'''