"""
@Time       ：2022/3/9 13:09 
@File       ：control.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""
from audio_record import audio_record
from wyy_controller import play_song
from wyy_controller import pause

pauseCommands = ["暂停", "停止", "取消"]


def command_analyse(text):
    for command in pauseCommands:
        if command in text:
            pause()
            return
    idx = text.find("播放")
    if idx != -1:
        idx += 2
        order = text[idx:idx + 3]
        play_song(order)



def start():
    while True:
        print("================================")
        print("请在三秒内说出指令:")
        audio_path = "./audio/test_audio.wav"
        audio_record(audio_path, 3)
        print("正在识别")
        from AipSpeech import audio_discern
        asr_result = audio_discern(audio_path)
        print(asr_result)
        command_text = asr_result['result'][0]
        command_analyse(command_text)


if __name__ == '__main__':
    start()
