"""
To filter unique records
"""
import pandas as pd

df = pd.read_excel("PYTHON_SAMPLE_FILE.xlsx")
df = df.drop_duplicates(subset=None, keep='first', inplace=False)
df['TRADE_DATE'] =  df['TRADE_DATE'].dt.date
writer = pd.ExcelWriter('output.xlsx')

df.to_excel(writer,'Sheet1')
writer.save()
