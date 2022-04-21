"""
@Time       ：2022/2/20 17:03 
@File       ：test.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "test sth"
"""
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from PIL import Image
import pyecharts_snapshot
import snapshot_phantomjs
from db import Db
import pyautogui
import time
import pyperclip
import utils
import re
import pandas as pd
import numpy as np
from pyecharts import Pie, configure
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

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图示例")
    pie.add(
        "",
        attr,
        v1,
        is_label_show=True,
        is_more_utils=True
    )
    path = 'E:\\speech_recognition_control_cloudMusic\\imgs\\饼图.jpeg'
    # pie.render(path=path)
    image = Image.open(r'E:\\speech_recognition_control_cloudMusic\\imgs\\test.jpg')
    image.show()
