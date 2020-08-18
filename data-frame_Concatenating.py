import numpy as np
import pandas as pd

surveys_df = pd.read_csv("./surveys.csv", keep_default_na=False, na_values=[""])

''' 
Take note that the read_csv method we used can take some additional options which we didn’t use previously. Many functions in Python have a set of options that can be set by the user if needed. In this case, we have told pandas to assign empty values in our CSV to NaN keep_default_na=False, na_values=[""]. '''

# Concatenating DataFrames

# Read in first 10 lines of surveys table
survey_sub = surveys_df.head(10)
print(survey_sub)

'''
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  weight
0          1      7   16  1977        2         NL   M             32.0     NaN
1          2      7   16  1977        3         NL   M             33.0     NaN
2          3      7   16  1977        2         DM   F             37.0     NaN
3          4      7   16  1977        7         DM   M             36.0     NaN
4          5      7   16  1977        3         DM   M             35.0     NaN
5          6      7   16  1977        1         PF   M             14.0     NaN
6          7      7   16  1977        2         PE   F              NaN     NaN
7          8      7   16  1977        1         DM   M             37.0     NaN
8          9      7   16  1977        1         DM   F             34.0     NaN
9         10      7   16  1977        6         PF   F             20.0     NaN

'''

# Exericises from https://datacarpentry.org/python-ecology-lesson/05-merging-data/
