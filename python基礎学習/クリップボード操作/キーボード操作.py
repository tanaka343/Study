from pynput.keyboard import Key, Controller
from pynput import keyboard

keyboard = Controller()

# #Aと入力（キーボードを押す離すでワンセット）
# keyboard.press("A")
# keyboard.release("A")

# #shift押しながらaでA
# with keyboard.pressed(Key.shift):
#     keyboard.press("a")
#     keyboard.release("a")

def on_press(key):
    try:
        # キーが文字の場合、その文字を入力
        keyboard.press(key.char)
        keyboard.release(key.char)
    except AttributeError:
        # 特殊キーの場合はそのまま入力
        keyboard.press(key)
        keyboard.release(key)   
    
def on_release(key):
    # Escキーが押されたらリスナーを停止
    if key == keyboard.Key.esc:
        return False                
# キーボードのリスナーを開始
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
