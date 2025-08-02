import pyperclip

pyperclip.copy('text to be copied')##クリップボードに書き込み
print(pyperclip.paste())##クリップボード情報取得

pyperclip.copy('')
print(pyperclip.waitForNewPaste())