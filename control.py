"""
@Time       ：2022/3/9 13:09 
@File       ：control.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "指令分发"
"""
import sys
import time
import utils
from audio_record import audio_record
from AipSpeech import audio_discern
from wyyController import play_song, find_songs, pause, set_wyy, play_fm, check_wyy
import re

pauseCommands = ["暂停", "停止", "取消"]
normalCommands = ['放大', '缩小', '关闭', '最小化']
mouseCommands = {'向上': 5, '向下': -5}


def command_analyse(text):
    # 歌手匹配 按歌手名搜索歌曲的可能
    match_obj = re.match(r'(.*播放|.*听)?(.+)的歌(.*)', text, re.I)
    if match_obj:
        singer = match_obj.group(2)
        find_songs(singer)
        return

    # 暂停歌曲的指令判断
    for command in pauseCommands:
        if command in text:
            pause()
            return

    # 控制鼠标滑轮的滑动
    for command in mouseCommands:
        if text.find(command) != -1:
            utils.mouse_scroll(mouseCommands[command])

    # 播放 or 切歌
    idx = text.find("播放")
    if idx != -1:
        if len(text) == 2:
            pause()
        else:
            idx += 2
            play_song(idx, text)
        return

    if text in normalCommands:
        set_wyy(text)
        return

    if '私人FM' in text:
        play_fm()
        return

    elif '查看' in text:
        check_wyy(text)
        return


def start():
    sec = 3
    while True:
        if sec > 8:
            # 如果等待时间过长 则停止程序
            print('SORRY, WAIT TOO LONG TIME!')
            sys.exit(0)
        print("================================")
        print("请在三秒内说出指令:")
        audio_path = "./audio/test_audio.wav"
        audio_record(audio_path, sec)
        print("正在识别")
        asr_result = audio_discern(audio_path)
        time.sleep(1)
        print(asr_result)
        try:
            command_text = asr_result['result'][0]
            if command_text == "停止运行":
                sys.exit(0)
            command_analyse(command_text)
        except KeyError:
            print("没听请, 请您再说一次")
            sec += 1


if __name__ == '__main__':
    start()
