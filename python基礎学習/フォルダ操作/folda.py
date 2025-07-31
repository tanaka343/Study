# import os

# current_dir=os.getcwd()
# print(f'ディレクトリ{current_dir}')

# file_path='python基礎学習/api_sap.py'
# if os.path.exists(file_path):
#     print('Yes')
# else:
#     print('No')

# new_folder='new_directory'
# if not os.path.exists(new_folder):
#     os.mkdir(new_folder)
# else:
#     print('既に存在します')

# import os
# import datetime

# file_path = "python基礎学習/api_sap.py"  # 対象ファイルのパス
# creation_time = os.path.getctime(file_path)  # 作成日時を取得
# formatted_time = datetime.datetime.fromtimestamp(creation_time)

# print(f"作成日時: {formatted_time}")

# from pathlib import Path
# import datetime

# file_path = Path("python基礎学習/api_sap.py")  # 対象ファイルのパス
# creation_time = file_path.stat().st_ctime  # 作成日時を取得
# formatted_time = datetime.datetime.fromtimestamp(creation_time)

# print(f"作成日時: {formatted_time}")

# 
# import os

# folder_path = "python基礎学習"  # フォルダのパスを指定
# file_names = []

# for root, dirs, files in os.walk(folder_path):
#     file_names.extend(files)
# print(file_names)


from pathlib import Path

folder_path = Path("python基礎学習")  # フォルダのパスを指定
file_names = [file.name for file in folder_path.iterdir() if file.is_file()]

print(file_names)
