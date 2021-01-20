### Google drive gives warning about not being able to scan with following code - COULD NOT READ WITH 15 mint of research - 19-Jan-2021

```
g_drive_url = 'https://drive.google.com/file/d/179KnOUR-GTPl2SQRte4imcWV5XAHVvFS/view?usp=sharing'

file_id = g_drive_url.split('/')[-2]

dwn_url='https://drive.google.com/uc?export=download&id=' + file_id

url = requests.get(dwn_url).text

csv_raw = StringIO(url)

donor_choose_df_org  = pd.read_csv(csv_raw, nrows=5000)
```
