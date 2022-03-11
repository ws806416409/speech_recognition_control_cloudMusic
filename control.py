"""
@Time       ：2022/3/9 13:09 
@File       ：control.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""
import sys
import time

from audio_record import audio_record
from AipSpeech import audio_discern
from wyy_controller import play_song
from wyy_controller import pause

pauseCommands = ["暂停", "停止", "取消", "暂停播放"]


def command_analyse(text):
    if text == "":
        print("NULL值")
    for command in pauseCommands:
        if command in text:
            pause()
            return
    idx = text.find("播放")
    if idx != -1:
        if len(text) == 2:
            pause()
        idx += 2
        play_song(idx, text)


def start():
    while True:
        print("================================")
        print("请在五秒内说出指令:")
        audio_path = "./audio/test_audio.wav"
        audio_record(audio_path, 5)
        print("正在识别")
        asr_result = audio_discern(audio_path)
        time.sleep(1)
        print(asr_result)
        command_text = asr_result['result'][0]
        if command_text == "停止运行":
            sys.exit(0)
        command_analyse(command_text)


if __name__ == '__main__':
    start()
