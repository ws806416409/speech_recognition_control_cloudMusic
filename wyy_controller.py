"""
@Time       ：2022/3/10 22:58 
@File       ：wyy_controller.py
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""

from pymouse import PyMouse
from pykeyboard import PyKeyboard


ms = PyMouse()
kb = PyKeyboard()


def find_song(name):
    pass


def play_all():
    pass


def pause():
    kb.press_key(kb.control_key)
    kb.tap_key('p')
    kb.release_key(kb.control_key)


def play_song(idx, text):
    order = text[idx:idx + 3]
    if order == "上一首":
        kb.press_key(kb.control_key)
        kb.tap_key(kb.left_key)
        kb.release_key(kb.control_key)
    elif order == "下一首":
        kb.press_key(kb.control_key)
        kb.tap_key(kb.right_key)
        kb.release_key(kb.control_key)
    elif text == "播放全部":
        play_all()
    else:
        find_song(order)
