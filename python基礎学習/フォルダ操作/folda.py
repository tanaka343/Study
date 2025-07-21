import os

current_dir=os.getcwd()
print(f'ディレクトリ{current_dir}')

file_path='python基礎学習/api_sap.py'
if os.path.exists(file_path):
    print('Yes')
else:
    print('No')

new_folder='new_directory'
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
else:
    print('既に存在します')
