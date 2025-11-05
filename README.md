# MacOS微信朋友圈自动点赞

1. 环境：

   > Python=3.13.3
   >
   > macOS=15.5
   >
   > wechat=4.1.1.18

2. 参数设置：

   > attempsTime设置一下循环次数
   >
   > my_friend_club.png 替换成自己的朋友圈封面和内容交界线这里
   >
   > + 这张图主要是为了聚焦朋友圈窗口

3. 运行命令 （在start文件里面也有）

   > python3 -m venv venv
   >
   > pip install pyautogui
   >
   > pip install pillow opencv-python
   >
   > chmod +x script.py
   >
   > ./script.py