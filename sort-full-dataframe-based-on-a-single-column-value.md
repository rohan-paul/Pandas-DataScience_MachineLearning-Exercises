### sort a dataframe in descending order based on the "proba" column, by using the sort_values() function:

```
data = pd.read_csv("some.csv")

data = data.sort_values( by= ["proba"], ascending = False)

```
