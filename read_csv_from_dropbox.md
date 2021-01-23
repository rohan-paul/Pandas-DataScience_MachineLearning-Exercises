### Dropbox

Saw that from dropbox, I can not read .zip file, but can read .csv

https://stackoverflow.com/a/48987986/1902852

#### You need to append `?dl=1` to the end of your url instead for `?dl=0`

```python
path = 'https://www.dropbox.com/s/7cg5eluc66iqlru/preprocessed-test.csv?dl=1'

df = pd.read_csv(path)
df.head(2)
```

#### For getting the link to share from Dropbox

Click on the horizontal dots > Share > Click and Copy Link > Then the Link will be generated > Click on Copy Link
