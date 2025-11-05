#!/usr/bin/env python3

import pyautogui

# 移动鼠标到指定坐标（100, 200）
# pyautogui.moveTo(100, 200, duration=0.3)

# 鼠标点击（左键），次数、间隔
# pyautogui.click(clicks=1, interval=0.1, button='left')

# 输入文本
# pyautogui.write("Hello WeChat", interval=0.05)

# 键盘按键
# pyautogui.press("enter")

# mac屏幕
scale = 0.5  # Retina 双倍屏幕


# 截图（返回PIL对象）
img = pyautogui.screenshot()


# 保存截图
img.save("screen.png")

# 滚轮
# pyautogui.scroll(-1000) 

# 查找屏幕上的图片，返回位置
loc = pyautogui.locateOnScreen("wechat.png", confidence=0.8)
if loc:
    pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)

loc = pyautogui.locateOnScreen("circle.png", confidence=0.8)
if loc:
    pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)

loc = pyautogui.locateOnScreen("test.png", confidence=0.6)
if loc:
    pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)

if loc:
    # 整屏截图
    img = pyautogui.screenshot()

    # 裁剪矩形区域 (left, top, right, bottom)
    crop = img.crop((
        loc.left,
        loc.top,
        loc.left + loc.width,
        loc.top + loc.height
    ))

    # 保存
    crop.save("found_like_button.png")
    print("Saved:", "found_like_button.png")
else:
    print("Not found")