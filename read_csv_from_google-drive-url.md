### Google drive gives warning about not being able to scan with following code - COULD NOT READ WITH 15 mint of research - 19-Jan-2021

```
g_drive_url = 'https://drive.google.com/file/d/179KnOUR-GTPl2SQRte4imcWV5XAHVvFS/view?usp=sharing'

file_id = g_drive_url.split('/')[-2]

dwn_url='https://drive.google.com/uc?export=download&id=' + file_id

url = requests.get(dwn_url).text

csv_raw = StringIO(url)

donor_choose_df_org  = pd.read_csv(csv_raw, nrows=5000)
```

```
<!DOCTYPE html><html><head><meta name="google" content="notranslate"><meta http-equiv="X-UA-Compatible" content="IE=edge;"><style>@font-face{font-family:'Roboto';font-style:italic;font-weight:400;src:url(//fonts.gstatic.com/s/roboto/v18/KFOkCnqEu92Fr1Mu51xIIzc.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:normal;font-weight:300;src:url(//fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmSU5fBBc9.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;src:url(//fonts.gstatic.com/s/roboto/v18/KFOmCnqEu92Fr1Mu4mxP.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:normal;font-weight:700;src:url(//fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmWUlfBBc9.ttf)format('truetype');}</style><meta name="referrer" content="origin"><title>train.zip - Google Drive</title><meta property="og:title" content="train.zip"><meta property="og:type" content="article"><meta property="og:site_name" content="Google Docs"><meta property="og:url" content="https://drive.google.com/file/d/1-BnjmSpTyQn5fSl0N5Gs2OWAZu16UJwN/view?usp=sharing&amp;usp=embed_facebook"><link rel="shortcut icon" href="https://ssl.gstatic.com/images/branding/product/1x/drive_2020q4_32dp.png"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Google+Sans:300
```

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
