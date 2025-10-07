import pyperclip
import time
from pynput import keyboard
# pyperclip.copy('text to be copied')##クリップボードに書き込み
# print(pyperclip.paste())##クリップボード情報取得

clip_list=[]
pyperclip.copy('')
A=pyperclip.paste()
while True:
    time.sleep(0.5)
    a=pyperclip.paste()
    if a != A:
        
        clip_list.append(a)
        A = a
        print(clip_list)