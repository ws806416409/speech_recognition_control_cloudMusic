"""
@Time       ：2022/3/9 13:09 
@File       ：control.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""
from audio_record import audio_record


def start():
    while(True):
        print("================================")
        print("请在三秒内说出指令:")
        audio_record("COMMAND", 3)
        print("正在识别")


if __name__ == '__main__':
    start()