# -*- coding: utf-8 -*-
pkg_name = "xpkg_demo" # 本包名称

import sys  # 检查是不是 python3
if sys.version_info.major < 3:
   print("Use python3 to run this file!")
   exit()

class Colors:
   BLACK = "\033[0;30m"
   RED = "\033[0;31m"
   GREEN = "\033[0;32m"
   BROWN = "\033[0;33m"
   BLUE = "\033[0;34m"
   PURPLE = "\033[0;35m"
   CYAN = "\033[0;36m"
   LIGHT_GRAY = "\033[0;37m"
   DARK_GRAY = "\033[1;30m"
   LIGHT_RED = "\033[1;31m"
   LIGHT_GREEN = "\033[1;32m"
   YELLOW = "\033[1;33m"
   LIGHT_BLUE = "\033[1;34m"
   LIGHT_PURPLE = "\033[1;35m"
   LIGHT_CYAN = "\033[1;36m"
   LIGHT_WHITE = "\033[1;37m"
   BOLD = "\033[1m"
   FAINT = "\033[2m"
   ITALIC = "\033[3m"
   UNDERLINE = "\033[4m"
   BLINK = "\033[5m"
   NEGATIVE = "\033[7m"
   CROSSED = "\033[9m"
   END = "\033[0m"

import os
import subprocess

# 开始本包的安装配置
# 得到ROS版本
ROS_VERSION = os.getenv('ROS_VERSION')
if (ROS_VERSION is None):
   print(Colors.RED + Colors.BLINK + Colors.BOLD + "Unknown ROS Verison! Please install the ros_environment package and source the /opt/ros/YOUR-ROS-VERSION/setup.bash" + Colors.END)
   print(ROS_VERSION)
   raise RuntimeError
ROS_VERSION = int(ROS_VERSION)
# 得到本python文件的路径
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

'''
这里放ROS1与ROS2都需要的安装步骤(apt装包, udev等)
'''
print(Colors.GREEN + "Install " + pkg_name + Colors.END)
if ROS_VERSION == 1:
   # 开始执行ROS1的安装需要
   ROS_DISTRO = os.getenv('ROS_DISTRO')
   subprocess.call(["sudo", "apt-get", "install", f"ros-{ROS_DISTRO}-teleop-twist-keyboard", "-y"])
   pass
elif ROS_VERSION == 2:
   # 开始执行ROS2的安装需要
   pass
else:
   print(Colors.BLINK + Colors.BOLD + Colors.NEGATIVE + Colors.RED + "Unknown ROS Verison! Please install the ros_environment package and source the /opt/ros/YOUR-ROS-VERSION/setup.bash" + Colors.END)
   print(ROS_VERSION)
   raise RuntimeError
print(Colors.GREEN + "Install " + pkg_name + " finish\n" + Colors.END)
