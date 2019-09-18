import random

import uiautomation
from PIL import ImageGrab,Image
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from My_opencv.a_01 import *

class Image_Frame1():

    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.opencv = ImageMathOpenCV(0.8)


    #随机坐标
    def get_position(self):

        #找浏览器的窗口
        cal_window = uiautomation.WindowControl(searchDepth=1,ClassName = "MozillaWindowClass")
        if cal_window.Exists():
            result = cal_window.BoundingRectangle
            x = random.randint(100,999)
            y = random.randint(100,999)
            return x,y


    def sele(self):


        x,y = self.zb("5.png")
        # print(1)
        self.mouse.click(x,y)
        self.keyboard.type_string("java")



    def open(self):
        x,y = self.zb("6.png")

        self.mouse.click(x,y)
        time.sleep(2)

        x1,y1 = self.zb("7.png")
        print(x1,y1)
        if x1 !=- 1 and y1 !=- 1:
            print("测试成功")








    #模拟鼠标左键单击
    def left_click(self):
        x,y = self.get_position()
        self.mouse.click(x,y,button=1,n=1)
        print("在位置%d,%d左键点击"%(x,y))
        return x,y



    #鼠标左键双击
    #模拟鼠标左键双击
    def left_double_click(self):
        x,y = self.get_position()
        self.mouse.click(x,y,button=1,n=2)
        print("在位置%d,%d左键双击"%(x,y))
        return x,y




    #滚动
    def top(self,num):
        self.mouse.scroll(vertical=num)




    #输入随机字符串

     #模拟使用键盘产生随机输入
    def input_string(self):
        result = []
        x,y = self.get_position()
        self.mouse.move(x,y)
        string = ["123","456","789"]
        index = random.randint(0,len(string)-1)
        key = string[index]
        self.keyboard.type_string(key)
        print("模拟使用键盘产生随机输入%s"%(key))
        result.append(x)
        result.append(y)
        return result,key



    #键盘按键(单键和组合键)
     #模拟使用键盘随机按键
    def enter_key(self):
        result = []
        x,y = self.get_position()
        self.mouse.move(x,y)
        keys = ["a","b","c","d","r",self.keyboard.numpad_keys[2]]
        index = random.randint(0,len(keys)-1)
        key = keys[index]
        self.keyboard.press_key(key)
        self.keyboard.release_key(key)
        print("模拟使用键盘按%s键"%(key))
        result.append(x)
        result.append(y)
        return result,key





    #获取坐标  图像识别的方式
    def zb(self,img):
     x,y = self.opencv.match_opencv(img)
     return x,y




if __name__ == '__main__':
    im1 = Image_Frame1()
    im1.sele()
    time.sleep(2)
    im1.open()