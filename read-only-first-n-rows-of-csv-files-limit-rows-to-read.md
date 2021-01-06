If you only want to read the first 999,999 (non-header) rows:

```
read_csv(..., nrows=999999)

```

If you only want to read rows 1,000,000 ... 1,999,999

```
read_csv(..., skiprows=1000000, nrows=999999)

```

nrows : int, default None Number of rows of file to read. Useful for reading pieces of large files\*

skiprows : list-like or integer Row numbers to skip (0-indexed) or number of rows to skip (int) at the start of the file

and for large files, you'll probably also want to use chunksize:

chunksize : int, default None Return TextFileReader object for iteration

[pandas.io.parsers.read_csv documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

https://stackoverflow.com/a/23853569/1902852
