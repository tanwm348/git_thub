import os
import random
import subprocess
from PIL import Image,ImageGrab
import time
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import uiautomation
import multiprocessing


class EasyMokey():
    def __init__(self):
        # 实例化鼠标,键盘对象
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()

    #随机坐标
    def get_position(self):

        #找浏览器的窗口
        cal_window = uiautomation.WindowControl(searchDepth=1,ClassName = "MozillaWindowClass")
        if cal_window.Exists():
            result = cal_window.BoundingRectangle
            x = random.randint(100,999)
            y = random.randint(100,999)
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
            # nowtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            # f.write(nowtime)
            f.write(info)
            f.write("\n")


    def start(self,count):
        execute = r"D:\woniu\Software\firefox.exe https://www.baidu.com"

        # 启动应用程序  start/b-不阻塞当前线程 不影响其他操作
        os.system("start/b %s"%(execute))


        for i in range(count):
            num = random.randint(0,5)
            num1 = random.randint(10,100)
            if num == 1:
                lc = self.left_click()
                self.report("id:%d,坐标:%s,鼠标操作:左键单击"%(num1,lc))

            elif num == 2:
                dc = self.left_double_click()
                self.report("id=%d,坐标=%s,操作=左键双击"%(num1,dc))

            elif num == 3:
                rc = self.right_click()
                self.report("id=%d,坐标=%s,操作=右键点击"%(num1,rc))

            elif num == 4:
                ek = self.enter_key()
                ek1 = ek[0]
                ek2 = ek[1]
                self.report("id=%d,坐标=%s,操作:键盘按了%s键"%(num1,ek1,ek2))

            elif num == 5:
                ist = self.input_string()
                ist1 = ist[0]
                ist2 = ist[1]
                self.report("id=%d,坐标=%s,操作=键盘输入%s"%(num1,ist1,ist2))



    def check(self,process):
        #获取当前正在运行的进程
        tasklist = subprocess.check_output("tasklist").decode("GBK")
        while True:
            #判断进程是否在执行
            if process in tasklist:
                print("%s 正在执行中..."%(process))
                #找被测窗口
                cal_window = uiautomation.WindowControl(searchDepth=1,ClassName = "MozillaWindowClass")
                print(cal_window)

                if cal_window.Exists():
                    #激活

                    time.sleep(2)
                    cal_window.SetActive()
                    # 置顶

                    cal_window.SetTopmost()
                    #最大化
                    cal_window.Maximize()
                    nowtime=time.strftime("%Y%m%d_%H_%M_%S",time.localtime(time.time()))

                    time.sleep(2)
                    #截图
                    image_path = os.path.abspath(".")+"//screen_shot//"+nowtime+"_img.png"
                    ImageGrab.grab().save(image_path)
                    break
                else:
                    print("找不到该窗口")
            else:
                print("进程已关闭")




    def read(self):
        newline1 = []


        with open("report1.txt","r",encoding="utf8") as f:
            while True:

              newline = f.readline()
              if newline == "":
                 break
              newline= newline.split("\n")
              newline1.append(newline)
            return newline1



    def get_valus(self):
        a = self.read()
        b=[]
        num = 0

        # input1 = input("输入id")
        for i in a:
               b.append(i)
               # print(b[num][0][3:5:1])
               # if b[num][0][3:5:1] == input1:
               result = b[num][0][20:22:1]
               # print(result)
               # 判断操作r45r456
               if result == "鼠标":

                   if b[num][0][25:29:1] == "右键单击":
                       print(1)
                       # print(b[num][0][25:29:1])
                       x = int(b[num][0][10:13:1])
                       y = int(b[num][0][14:18:1])
                       # print(x,y)
                       self.mouse.click(x,y,button=2,n=1)

                   elif b[num][0][25:29:1] == "左键单击":
                       print(2)
                       # print(b[num][0][25:29:1])
                       x = int(b[num][0][10:13:1])
                       y = int(b[num][0][14:18:1])
                       # print(x,y)
                       self.mouse.click(x,y,button=1,n=1)


                   else:
                       print(3)
                       x = int(b[num][0][10:13:1])
                       y = int(b[num][0][14:18:1])
                       # print(x,y)
                       self.mouse.click(x,y,button=1,n=2)


               elif result == "键盘":
                   print(4)
                   # print(b[num][0][27:29:1])
                   # id=78,坐标=[324, 318],键盘操作:键盘按了r键
                   if b[num][0][27:29:1] == "输入":
                       # print(b[num][0][29:31:1])
                       self.keyboard.type_string(b[num][0][29:32:1])

                   else:
                       print(5)
                       self.keyboard.press_key(b[num][0][29:30:1])
                       self.keyboard.release_key(b[num][0][29:30:1])
                       # print(3)

               num+=1








if __name__ == '__main__':
    ek = EasyMokey()
    # ek.start(10,"calc.exe")#打开计算机
    # ek.start(1,"notepad")#打开记事本
    # ek.start(10,"Firefox.exe")
    # ek.start(10)
    # m1 = multiprocessing.Process(target=ek.start,args=(10,))
    # m2 = multiprocessing.Process(target=ek.check,args=("firefox.exe",))
    # ek.check("firefox.exe")
    # m1.start()
    # m1.join()
    # m2.start()
    # m2.join()
    ek.get_valus()

