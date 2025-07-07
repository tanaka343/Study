from flask import Flask,render_template,redirect
import pandas as pd

app = Flask(__name__)

@app.route('/')
def top():
  df=pd.read_excel(r"C:\Users\hyom0\OneDrive\デスクトップ\【入力シート】全国の放課後等デイサービス事業所リスト作成.xlsx",sheet_name='都島区', names=["houjin_name","jigyousyo_name","email","phone","website"])
  facility_list=df.to_dict()
  num=len(facility_list)
  return render_template('index.html',facility_list=facility_list,num=num)
  





if __name__ == "__main__":

  app.run()


# df=pd.read_excel(r"C:\Users\hyom0\OneDrive\デスクトップ\【入力シート】全国の放課後等デイサービス事業所リスト作成.xlsx",sheet_name='都島区', names=["houjin_name","jigyousyo_name","email","phone","website"])
# df_dict=df.to_dict

