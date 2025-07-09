from flask import Flask,render_template,redirect,send_from_directory,request,session,send_file
import pandas as pd
import os
import openpyxl
import io

app = Flask(__name__)
app.secret_key =os.urandom(24).hex()

@app.route('/')
def top():
  df=pd.read_excel(r"C:\Users\Guest User\OneDrive\デスクトップ\【入力シート】全国の放課後等デイサービス事業所リスト作成 のコピー.xlsx",sheet_name='都島区', names=["houjin_name","jigyousyo_name","email","phone","website"])
  facility_list=df.to_dict(orient='records')
  session['my_dataframe']=df.to_json(orient='split')
  
  return render_template('index.html',facility_list=facility_list,)
  



DOWNLOAD_DIR_PATH = os.getenv("DOWNLOAD_DIR_PATH")
base_dir = os.path.dirname(__file__)
DOWNLOAD_DIR_PATH = os.path.join(base_dir,'自動化アプリ出力')
XLSX_MIMETYPE='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
CSV_MIMETYPE = 'text/csv'
@app.route('/download', methods=['GET','POST'])
def download():

    if request.method=='POST':
      json_data = session.get('my_dataframe')
      df=pd.read_json(json_data,orient='split')
      download_type=request.form.get('download')
      output_buffer = io.BytesIO()
      if download_type=="csv":
        df.to_csv(output_buffer,index=False)
        downloadFileName ='テストcsv'
        downloadFile = 'to_csv_out.csv'
        file_mimetype = CSV_MIMETYPE
      elif download_type=="excel":
        # df.to_excel('自動化アプリ出力/to_excel_out.xlsx')
        downloadFileName ='テストexcel.xlsx'
        downloadFile = 'to_excel_out.xlsx'
        file_mimetype =XLSX_MIMETYPE
        with pd.ExcelWriter(output_buffer, engine='openpyxl') as writer:
          df.to_excel(writer, index=False, sheet_name='データ')

      
      output_buffer.seek(0)
      # session.pop('my_dataframe', None) 

      return send_file(output_buffer, \
          mimetype = file_mimetype,as_attachment = True, download_name = downloadFileName
          )
    return redirect('/')


if __name__ == "__main__":

  app.run()


# df=pd.read_excel(r"C:\Users\hyom0\OneDrive\デスクトップ\【入力シート】全国の放課後等デイサービス事業所リスト作成.xlsx",sheet_name='都島区', names=["houjin_name","jigyousyo_name","email","phone","website"])
# df_dict=df.to_dict

