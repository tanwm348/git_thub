import os
import random

import time
from pykeyboard import PyKeyboard
from pymouse import PyMouse

class EasyMokey():
    def __init__(self):
        # 实例化鼠标,键盘对象
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()

    #随机坐标
    def get_position(self):
        x = random.randint(0,1600)
        y = random.randint(0,900)
        return x,y

    #模拟鼠标左键单击
    def left_click(self):
        x,y = self.get_position()
        self.mouse.click(x,y,button=1,n=1)
        print("在位置%d,%d左键点击"%(x,y))
        return x,y


    #模拟鼠标左键双击
    def left_double_click(self):
        x,y = self.get_position()
        self.mouse.click(x,y,button=1,n=2)
        print("在位置%d,%d左键双击"%(x,y))
        return x,y

    #模拟鼠标右键单击
    def right_click(self):
        x,y = self.get_position()
        self.mouse.click(x,y,button=2,n=1)
        print("在位置%d,%d右键点击"%(x,y))
        return x,y



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




    def report(self,info):
         with open("report1.txt","a",encoding="utf8") as f:
            nowtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            f.write(nowtime)
            f.write(info)
            f.write("\n")


    def start(self,count):

        #启动应用程序  start/b-不阻塞当前线程 不影响其他操作
        # os.system("start/b %s"%(execute))


        for i in range(count):
            num = random.randint(0,5)
            num1 = random.randint(1,100)
            if num == 1:
                lc = self.left_click()
                self.report("选择了%d,左键点击的id为%d,坐标为%s,左键单击"%(num,num1,lc))

            elif num == 2:
                dc = self.left_double_click()
                self.report("选择了%d,左键双击的id为%d,坐标为%s,左键双击"%(num,num1,dc))

            elif num == 3:
                rc = self.right_click()
                self.report("选择了%d,右键点击的id为%d,坐标为%s,右键点击"%(num,num1,rc))

            elif num == 4:
                ek = self.enter_key()
                ek1 = ek[0]
                ek2 = ek[1]
                self.report("选择了%d,模拟键盘按键id为%d,坐标为%s,模拟使用键盘按了%s键"%(num,num1,ek1,ek2))

            elif num == 5:
                ist = self.input_string()
                ist1 = ist[0]
                ist2 = ist[1]
                self.report("选择了%d,模拟键盘输入id为%d,坐标为%s,模拟使用键盘输入了%s"%(num,num1,ist1,ist2))






if __name__ == '__main__':
    ek = EasyMokey()
    # ek.start(10,"calc.exe")#打开计算机
    # ek.start(1,"notepad")#打开记事本
    # ek.start(10,"Firefox.exe")
    ek.start(10)