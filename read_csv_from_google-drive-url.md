### Google drive gives warning about not being able to scan with following code - COULD NOT READ WITH 15 mint of research - 19-Jan-2021

Basically for small files, I have to pass the url in below format, i.e.

'https://drive.google.com/uc?export=download&id=' +'id_of_the_file'

```
https://drive.google.com/uc?export=download&id=1-WDVUwSdq5wKKCqnGl67EXz5u2BtRpR6

```

BUT ON 23-JAN-2021 AFTER 3 HOURS OF RESEARCH, I COULD NOT FIND A WAY TO READ CSV FILES ( > 100 mb ) LIKE THIS WAY. SEEMS LIKE THERE'S NONE.

Only way is to use some form of actually downloading the file in local drive by invoking google-auth api etc (for which there's a few pip packages)

#### Further Reading

https://stackoverflow.com/questions/64731772/in-python-how-to-read-a-large-csv-that-is-in-google-drive - This SO question was asked in Nov-2020 and remains unanswered.

https://stackoverflow.com/questions/56611698/pandas-how-to-read-csv-file-from-google-drive-public

---

Same instruction in YT Video which works only for smaller files - https://www.youtube.com/watch?v=UUYdEUBbmzU&ab_channel=IndianAIProduction

---

### Alternative - Dropbox

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
