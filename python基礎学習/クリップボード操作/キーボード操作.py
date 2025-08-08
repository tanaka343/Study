from pynput.keyboard import Key, Controller
from pynput import keyboard

keyboard = Controller()

#Aと入力（キーボードを押す離すでワンセット）
keyboard.press("A")
keyboard.release("A")

#shift押しながらaでA
with keyboard.pressed(Key.shift):
    keyboard.press("a")
    keyboard.release("a")

