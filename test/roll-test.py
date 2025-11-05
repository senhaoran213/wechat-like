#!/usr/bin/env python3

import pyautogui
# mac屏幕
scale = 0.5  # Retina 双倍屏幕

# 查找屏幕上的图片，返回位置
loc = pyautogui.locateOnScreen("wechat.png", confidence=0.8)
if loc:
    pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)
    # print(loc)    Box(left=np.int64(2021), top=np.int64(123), width=100, height=100)

loc = pyautogui.locateOnScreen("my_friend_club.png", confidence=0.8)
if loc:
    pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)
    # print(loc)    Box(left=np.int64(2021), top=np.int64(123), width=100, height=100)
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


# 滚轮
pyautogui.scroll(-6000) 