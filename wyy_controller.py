"""
@Time       ：2022/3/10 22:58 
@File       ：wyy_controller.py
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "网易云音乐后端操控接口"
"""
import time
import utils
import pyperclip
from pymouse import PyMouse
from pykeyboard import PyKeyboard


ms = PyMouse()
kb = PyKeyboard()


def find_song(songName):
    # size = ms.screen_size()
    # kb.type_string("渡口") 无法输出中文 换方法
    ms.click(450, 30, 1)
    # kb.type_string("Hotel California")
    pyperclip.copy("渡口")
    # 模拟粘贴 + 回车 搜索歌曲
    kb.press_key(kb.control_key)
    kb.tap_key('v')
    kb.release_key(kb.control_key)
    kb.tap_key(kb.enter_key)
    time.sleep(1)
    play_all()


# 点击播放全部
def play_all():
    utils.mouse_click('static/play_all.png')


# 暂停 or 恢复播放
def pause():
    kb.press_key(kb.control_key)
    kb.tap_key('p')
    kb.release_key(kb.control_key)


# 播放歌曲 上一首 下一首
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
        songName = text[idx:]
        find_song(songName)
