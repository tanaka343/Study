import os
import pathlib
import datetime
import time
import platform
from pathlib import Path

# p = pathlib.Path('python基礎学習/フォルダ操作/folder.py')
# print(p)
# print(type(p))

# p_file=pathlib.Path('python基礎学習/api_sap.py')
# print(p_file.suffix)

# print(p_file.exists())

# p_newfile= pathlib.Path('python基礎学習/test.py')

# p_newfile.touch()

# print(p_newfile.exists())

# pathlib.Path('python基礎学習/test.py').touch()

# p_newfile= pathlib.Path('python基礎学習/test.py')
# if p_newfile.exists() == False:
#   p_newfile.touch()
# else:
#   print('Yes')



# for p in pathlib.Path('python基礎学習').iterdir():
#   print(p)

# print(list(pathlib.Path('python基礎学習').iterdir()))

p= Path('plactice')
if p.exists()==False:
  p.mkdir()
p_newfile = pathlib.Path('plactice/test.txt')
if p_newfile.exists()==False:
  p_newfile.touch()

# p.rmdir()

p_newfile.write_text('test')
timestanp=p_newfile.stat()
last_kousin=timestanp.st_atime

import datetime

dt= datetime.datetime.fromtimestamp(last_kousin)

print(dt.date())
print(dt.time())

today = datetime.datetime.now()
print(today.date())

if today.date()==dt.date():
  print('Yes')
