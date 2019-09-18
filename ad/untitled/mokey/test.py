import os
import subprocess
from PIL import Image,ImageGrab

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

#模拟鼠标
#鼠标的操作  左键单击,左键双击,右键单击,滚轮
# 实例化鼠标对象
# mouse = PyMouse()
# x,y:点击坐标
# button   1 = left   2 = right   3 = middle(中间按键)
#n:点击数
# time.sleep(5)
# mouse.click(349,48,button = 1,n=2)


# #上下滚动  正数向上   负数向下
# mouse.scroll(vertical=10)
#
# #左右滚动 正数向右,负数向左
# mouse.scroll(horizontal=-10)
#
# #移动到指定坐标点
# mouse.move(697,531)

#模拟键盘的操作
#键盘操作 按下某个键,松开某个键,输入字符串,组合键


# #实例化键盘
# keboard = PyKeyboard()
# time.sleep(3)
# #按下a键
# keboard.press_key("a")
# #松开a键
# keboard.release_key("a")
#
# #按下F5   F+5
# keboard.press_key(keboard.function_keys[5])
# #释放
# keboard.release_key(keboard.function_keys[5])
#
# #数字
# keboard.press_key(keboard.numpad_keys[9])
# keboard.release_key(keboard.numpad_keys[9])


#回车,空格,shift
# keboard.press_key(keboard.shift_key)
# keboard.release_key(keboard.shift_key)

# keboard.press_key(keboard.space)
# keboard.release_key(keboard.space)
#
# time.sleep(1)
# #键盘输入
# for i in range(10000):
#  keboard.type_string("123")
#
#  keboard.press_key(keboard.space)
#  keboard.release_key(keboard.space)


#组合键
# keboard.press_key(keboard.control_key)
# keboard.press_key(keboard.space)
# keboard.press_key("a")
# keboard.release_key("a")








# Subprocess  # ---python自带的一个子进程模块


# subprocess.Popen()   #创建一个子进程去执行一个命令  不阻塞当前进程执行
# os.system("start/b calc.exe")
#
# # 保存命令执行的返回来的结果
# tasklist = subprocess.check_output("tasklist")
# print(tasklist.decode("GBK"))
#
# #判断应用正在运行
# if "calc.exe" in tasklist.decode("GBK"):
#        print("程序正在运行")
#
#
# #杀掉进程 taskkill
# subprocess.Popen("taskkill /IM cale.exe /F")
# print(tasklist.decode("GBK"))
#
#打开图片--返回对象
im = Image.open("C:\\Users\Administrator\Desktop\QQ截图20190715114920.png")
print(im)
#展示图片
# im.show()
#获取当前路径
folder = os.path.abspath(".")+"//screen_shot//"

#截图
im1 = ImageGrab.grab()
# im1.save("./screen_shot/3.png")
im1.save(folder+"/3.png")