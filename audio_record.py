"""
@Time       ：2022/2/20 16:29 
@File       ：audio_record.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "音频文件转存"
"""
import wave
import pyaudio


def audio_record(command_file, rec_time):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16  # 16bit 位深
    CHANNELS = 1  # 单声道
    RATE = 16000  # 采样频率

    p = pyaudio.PyAudio()

    # 创建音频流
    stream = p.open(
        frames_per_buffer=CHUNK,
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE
    )

    frames = []
    # 录制音频数据
    for i in range(0, int(RATE // CHUNK * rec_time)):
        data = stream.read(CHUNK)
        frames.append(data)

    # 结束录制
    stream.stop_stream()
    stream.close()
    p.terminate()

    # save
    wf = wave.open(command_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    audio_record()
