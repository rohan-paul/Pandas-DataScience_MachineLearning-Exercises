#### Handling Categorical Data in Python

https://www.tutorialspoint.com/python_pandas/python_pandas_categorical_data.htm

##### Often in real-time, data includes the text columns, which are repetitive. Features like gender, country, and codes are always repetitive. These are the examples for categorical data. These generally include different categories or levels associated with the observation, which are non-numerical and thus need to be converted so the computer can process them.

Categorical variables can take on only a limited, and usually fixed number of possible values. Besides the fixed length, categorical data might have an order but cannot perform numerical operation. Categorical are a Pandas data type.

The categorical data type is useful in the following cases −

A string variable consisting of only a few different values. Converting such a string variable to a categorical variable will save some memory.

The lexical order of a variable is not the same as the logical order (“one”, “two”, “three”). By converting to a categorical and specifying an order on the categories, sorting and min/max will use the logical order instead of the lexical order.

As a signal to other python libraries that this column should be treated as a categorical variable (e.g. to use suitable statistical methods or plot types).

---

https://www.kaggle.com/getting-started/27270
