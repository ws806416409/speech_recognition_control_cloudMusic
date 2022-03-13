"""
@Time       ：2022/3/9 13:09 
@File       ：control.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "指令分发"
"""
import sys
import time
from audio_record import audio_record
from AipSpeech import audio_discern
from wyy_controller import play_song, find_songs, pause
import re


pauseCommands = ["暂停", "停止", "取消"]


def command_analyse(text):
    # 歌手匹配 按歌手名搜索歌曲的可能
    match_obj = re.match(r'(.*播放|.*听)?(.+)的歌(.*)', '我要听陈奕迅的歌曲', re.I)
    if match_obj:
        singer = match_obj.group(2)
        find_songs(singer)
    # 暂停歌曲的指令判断
    for command in pauseCommands:
        if command in text:
            pause()
            return
    # 播放 or 切歌
    idx = text.find("播放")
    if idx != -1:
        if len(text) == 2:
            pause()
        idx += 2
        play_song(idx, text)


def start():
    while True:
        print("================================")
        print("请在三秒内说出指令:")
        audio_path = "./audio/test_audio.wav"
        audio_record(audio_path, 3)
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


if __name__ == '__main__':
    start()
