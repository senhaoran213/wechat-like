#!/usr/bin/env python3

import pyautogui
import time

# 给图片文件路径
more_btn_img = 'more.png'  # “更多”按钮截图
like_btn_img = 'like.png'  # 展开后的点赞按钮截图

# 等待切换到微信界面
time.sleep(3)

# 点击“更多”按钮
more_btn = pyautogui.locateCenterOnScreen(more_btn_img, confidence=0.8)
if more_btn:
    pyautogui.click(more_btn)
    print("点击了更多按钮")
    time.sleep(0.5)  # 等待展开动画
else:
    print("未找到更多按钮")

# 点击点赞按钮
like_btn = pyautogui.locateCenterOnScreen(like_btn_img, confidence=0.8)
if like_btn:
    pyautogui.click(like_btn)
    print("点击了点赞按钮")
else:
    print("未找到点赞按钮")