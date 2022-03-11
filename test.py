"""
@Time       ：2022/2/20 17:03 
@File       ：test.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "test sth"
"""
import win32gui
from pykeyboard import PyKeyboard


def word_count():
    with open('src.txt') as f:
        s = f.read()
        words = set(s.split(' '))
        print(len(words))



if __name__ == '__main__':
    name = "NetEase Cloud Music (32 位)"
    handle = win32gui.FindWindow(None, name)
    win32gui.SetForegroundWindow(handle)
