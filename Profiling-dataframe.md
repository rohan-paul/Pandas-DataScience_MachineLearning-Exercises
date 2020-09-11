## 1. Profiling the pandas dataframe

**Profiling** is a process that helps us in understanding our data and [**Pandas**](https://github.com/pandas-profiling/pandas-profiling)[**Profiling**](https://github.com/pandas-profiling/pandas-profiling) is python package which does exactly that. It is a simple and fast way to perform exploratory data analysis of a Pandas Dataframe. The pandas`df.describe()`and `df.info()functions` are normally used as a first step in the EDA process. However, it only gives a very basic overview of the data and doesn’t help much in the case of large data sets. The Pandas Profiling function, on the other hand, extends the pandas DataFrame with`df.profile_report()` for quick data analysis. It displays a lot of information with a single line of code and that too in an interactive HTML report.

For a given dataset the pandas profiling package computes the following statistics:

![](https://cdn-images-1.medium.com/max/800/1*T2iRcSpLLxXop7Naa4ln0g.png)

Statistics computer by Pandas Profiling package.

#### Installation

```
pip install pandas-profiling
or
conda install -c anaconda pandas-profiling`
```

#### Usage

Let’s use the age-old titanic dataset to demonstrate the capabilities of the versatile python profiler.

```
#importing the necessary packages
 import pandas as pd
 import pandas_profiling
```

To display the report in a Jupyter notebook, run

```
 df.profile_report()
```

This single line of code is all that you need to display the data profiling report in a Jupyter notebook. The report is pretty detailed including charts wherever necessary.

![](https://cdn-images-1.medium.com/max/800/1*iqLgI-YaaV4iE6LDySSE2g.gif)

The report can also be exported into an **interactive HTML file** with the following code.

```
profile = df.profile_report(title='Pandas Profiling Report')
profile.to_file(outputfile="Titanic data profiling.html")

```

![](https://cdn-images-1.medium.com/max/800/1*Oms7fW4rNlU0NaMUf9qYmA.gif)

Refer the [documentation](https://pandas-profiling.github.io/pandas-profiling/docs/) for more details and examples.
