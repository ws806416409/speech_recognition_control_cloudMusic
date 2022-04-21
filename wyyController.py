"""
@Time       ：2022/3/10 22:58 
@File       ：wyyController.py
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "网易云音乐后端操控接口"
"""
import time
import utils
import pyperclip
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pyecharts import Pie
from PIL import Image
import re

import wyySpider
from db import Db

ms = PyMouse()
kb = PyKeyboard()


# 查找歌曲
def find_songs(param):
    # size = ms.screen_size()
    # kb.type_string("渡口") 无法输出中文 换方法
    ms.click(450, 30, 1)
    # kb.type_string("Hotel California")
    pyperclip.copy(param)
    # 模拟粘贴 + 回车 搜索歌曲
    kb.press_key(kb.control_key)
    kb.tap_key('v')
    kb.release_key(kb.control_key)
    kb.tap_key(kb.enter_key)
    time.sleep(2)
    play_all()


# 点击播放全部
def play_all():
    utils.mouse_click('play_all.png')


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
        song_name = text[idx:]
        find_songs(song_name)


def add_like():
    kb.press_key(kb.control_key)
    kb.tap_key('l')
    kb.release_key(kb.control_key)


# 网易云基础设置
def set_wyy(command):
    if command in ['放大', '缩小']:
        pass
    elif command == '关闭':
        pass
    elif command == '最小化':
        pass


def play_fm():
    utils.mouse_click('static/FM.png')


def check_wyy(text):    
    # 复制歌曲链接
    ms.click(40, 1400, 1)
    time.sleep(1)
    utils.mouse_click('share.png')
    time.sleep(0.7)
    utils.mouse_click('link.png')
    # 提取歌曲sid(song_id)
    content = pyperclip.paste()
    print(content)
    sid = re.search(r'(song\?id=)(\d+)', content).group(2)
    # 爬虫 将信息写入文件
    wyySpider.main(sid)
    db = Db()
    # 爬虫数据中 0是未知 1是男 2是女
    if '性别比例' in text:
        unknown = 0
        male = 0
        female = 0
        gender_list = db.list("gender")
        for gender in gender_list:
            if gender == 0:
                unknown += 1
            elif gender == 1:
                male += 1
            else:
                female += 1
        attr = ["未知", "男", "女"]
        v1 = [unknown, male, female]
        pie = Pie("性别比例饼图")
        pie.add(
            "",
            attr,
            v1,
            is_label_show=True,
            is_more_utils=True
        )
        path = 'E:\\speech_recognition_control_cloudMusic\\imgs\\' + str(sid) + '性别比例.jpeg'
        pie.render(path=path)
        image = Image.open(path)
        image.show()



