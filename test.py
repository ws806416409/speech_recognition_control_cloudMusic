"""
@Time       ：2022/2/20 17:03 
@File       ：test.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : "test sth"
"""


def word_count():
    with open('src.txt') as f:
        s = f.read()
        words = set(s.split(' '))
        print(len(words))


if __name__ == '__main__':
    #word_count()
    text = "播放下一首"
    idx = text.find("播放")
    order = text[idx+2:idx+5]

    print(order)

