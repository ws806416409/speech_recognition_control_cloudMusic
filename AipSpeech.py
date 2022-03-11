"""
@Time       ：2022/3/9 13:26 
@File       ：AipSpeech.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""
from aip import AipSpeech


def audio_discern(audio_path, audio_type="wav"):
    APP_ID = 'xxxx'
    API_KEY = 'xxxxxx'
    SECRET_KEY = 'xxxxxxx'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 读取文件
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别本地文件
    text = client.asr(get_file_content(audio_path), audio_type, 16000, {'dev_pid': 1536, })
    return text
