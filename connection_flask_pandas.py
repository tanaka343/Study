from flask import Flask,render_template,redirect
import pandas as pd

app = Flask(__name__)

@app.route('/')
def top():
  df=pd.read_excel(r"C:\Users\Guest User\OneDrive\デスクトップ\【入力シート】全国の放課後等デイサービス事業所リスト作成 のコピー.xlsx",sheet_name='豊島区', names=["houjin_name","jigyousyo_name","email","phone","website"])
  facility_list=df.to_dict()
  return render_template('index.html',facility_list=facility_list)
  return 'HELLO'






if __name__ == "__main__":

  app.run()
