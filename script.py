#!/usr/bin/env python3

import pyautogui
# mac屏幕
scale = 0.5  # click方法里面的是逻辑像素 也就是单倍像素 
#滑动单位
slideUnit = 4000
attemptsNumber = 999

# 打开微信
loc = pyautogui.locateOnScreen("wechat.png", confidence=0.7)
if loc:
    pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)
    print('已打开微信图标')

# 打开朋友圈
# loc = pyautogui.locateOnScreen("circle.png", confidence=0.8)
# if loc:
#     pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)

loc = pyautogui.locateOnScreen("my_friend_club.png", confidence=0.8)
if loc:
    pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)
    print('已聚焦我的朋友圈')


# 查找更多按钮
def execute():
    try:
        loc = pyautogui.locateOnScreen("more.png", confidence=0.8)
        if loc:
            pyautogui.click((loc.left + loc.width/2)*scale, (loc.top + loc.height/2)*scale)
            print('已点击更多按钮')
            like = pyautogui.locateOnScreen("like.png", confidence=0.8)
            if like:
                pyautogui.click((like.left + like.width/2)*scale, (like.top + like.height/2)*scale)
                print('点赞+1')
                return True
            else:
                pyautogui.scroll(-slideUnit) 
                print('点过赞了下滑{slideUnit}单位')
                return False
        else:
            pyautogui.scroll(-slideUnit) 
            print('没找到更多按钮下滑{slideUnit}单位')
            return False
    except pyautogui.ImageNotFoundException:
        pyautogui.scroll(-slideUnit) 
        print('抓异常：没找到更多按钮下滑{slideUnit}单位')
        return False
    

        
# 主循环逻辑
for i in range(attemptsNumber):
    if execute():
        print(f"第 {i+1} 次执行，成功")
    else:
        print(f"第 {i+1} 次执行，失败")