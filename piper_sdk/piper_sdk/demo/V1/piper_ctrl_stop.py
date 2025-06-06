#!/usr/bin/env python3
# -*-coding:utf8-*-
# 注意demo无法直接运行，需要pip安装sdk后才能运行
# 设置机械臂重置，需要在mit或者示教模式切换为位置速度控制模式时执行
# 使用后需要reset，并重新使能两次

from typing import (
    Optional,
)
import time
from piper_sdk import *

# 测试代码
if __name__ == "__main__":
    piper = C_PiperInterface()
    piper.ConnectPort()
    piper.MotionCtrl_1(0x01, 0, 0)
