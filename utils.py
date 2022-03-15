"""
@Time       ：2022/3/11 22:09 
@File       ：utils.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""
import pyautogui


def mouse_scroll(clicks):
    pyautogui.scroll(clicks)


# 图像识别单击事件
def mouse_click(image):
    # 根据图片识别定位x,y坐标
    x, y = pyautogui.locateCenterOnScreen(image)
    print(x, y)
    pyautogui.click(x, y, clicks=1, interval=0.2, duration=0.2, button='left')

