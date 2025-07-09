import pandas as pd

pd.DataFrame({
  '名前':['佐藤','鈴木','斎藤'],
  '年齢':[21,30,18],
  '住所':['東京都','岐阜県','埼玉県']
},index=['i-1','i-2','i-3'])

pd.Series(
  ['佐藤','鈴木','斎藤'],
  index=['i-1','i-2','i-3']
)

df=pd.read_excel(r"C:\Users\Guest User\OneDrive\デスクトップ\【入力シート】全国の放課後等デイサービス事業所リスト作成 のコピー.xlsx",sheet_name='豊島区'
                  ,names=["houjin_name","jigyousyo_name","email","phone","website"])

print(df)