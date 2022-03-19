"""
@Time       ：2022/2/20 17:03 
@File       ：test.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "test sth"
"""
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyautogui
import time
import pyperclip
import utils
import re

import wyySpider

ms = PyMouse()
kb = PyKeyboard()


def word_count():
    with open('src.txt') as f:
        s = f.read()
        words = set(s.split(' '))
        print(len(words))


if __name__ == '__main__':
    # kb.type_string("Hotel California")
    '''
    pyperclip.copy("渡口")
    kb.press_key(kb.control_key)
    kb.tap_key('v')
    kb.release_key(kb.control_key)
    kb.tap_key(kb.enter_key)
    time.sleep(2)
    utils.mouse_click('play_all.png')
    matchSinger = re.match(r'(.*播放|.*听)?(.+)的歌(.*)', '播放渡口', re.I)
    if matchSinger:
        print("match success", matchSinger.group(2))
        print(matchSinger.group(1))
    else:
        print("false")
    '''
    wyySpider.main(1901371647)
