#!/usr/bin/env python3
import Quartz
import Quartz

def get_scale():
    main_id = Quartz.CGMainDisplayID()

    # 真实像素尺寸
    real_width = Quartz.CGDisplayPixelsWide(main_id)
    real_height = Quartz.CGDisplayPixelsHigh(main_id)

    # 逻辑尺寸（point）
    rect = Quartz.CGDisplayBounds(main_id)
    logical_width = rect.size.width
    logical_height = rect.size.height

    scale_x = real_width / logical_width
    scale_y = real_height / logical_height

    return scale_x  # 一般 x=y=2 对称屏幕

scale = get_scale()
print("Detected Scale:", scale)