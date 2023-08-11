import pyautogui
import time

# 设置点击的坐标和次数
click_x = 500
click_y = 500
num_clicks = 10

# 延时，以便切换到需要点击的窗口
time.sleep(5)

# 模拟点击操作
for _ in range(num_clicks):
    pyautogui.click(click_x, click_y)
    time.sleep(0.5)  # 可以根据需要调整点击间隔
