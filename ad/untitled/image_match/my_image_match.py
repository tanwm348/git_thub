import os
from pymouse import PyMouse
from PIL import ImageGrab,Image
import time
import math
class ImageMatch():
    def __init__(self):
        self.w = 0
        self.h = 0
        self.screen_pixes = None
        self.target_pixes = None
        self.mouse = PyMouse()



    def match_pixes(self,screen,target):
        # 比较两个点的4个通道的值GRBA
       if screen[0] == target[0] and screen[1] == target[1] and screen[2] == target[2] and screen[3] == target[3]:
           return True

       return False


    #比较模板图片和大图对应位置图片是所有点
    def match(self,x,y,simiarty):
        not_match = 0
        for target_x in range(0,self.w):
            for target_y in range(0,self.h):
                #如果有一个像素点不匹配,就认为不匹配
                if not self.match_pixes(self.target_pixes[target_x,target_y],self.screen_pixes[x+target_x,y+target_y]):
                    not_match+=1



        simi = ((self.w*self.h)-not_match)/(self.w*self.h)

        if simi >= simiarty:
            return True
        else:
            print(1)
            return False





    #从大图中寻找模板图片
    def find_image(self,image):
        #截取大图
        screen = ImageGrab.grab().convert("RGBA")


        #模板图片
        folder = os.path.abspath(".")+"//screen//"+image
        target = Image.open(folder)

        #获取模板图片和截图的像素值
        self.screen_pixes = screen.load()
        self.target_pixes =target.load()


        #获取模板照片和截图的大小
        W,H = screen.size
        self.w,self.h = target.size
        print(W,H,self.w,self.h)

        #滑动比对
        for x in range(W-self.w+1):
            for y in range(H-self.h+1):

                left_top=self.match_pixes(self.screen_pixes[x,y],self.target_pixes[0,0])
                right_top=self.match_pixes(self.screen_pixes[x+self.w-1,y],self.target_pixes[self.w-1,0])
                left_buttom=self.match_pixes(self.screen_pixes[x,y+self.h-1],self.target_pixes[0,self.h-1])
                right_buttom=self.match_pixes(self.screen_pixes[x+self.w-1,y+self.h-1],self.target_pixes[self.w-1,self.h-1])
                center=self.match_pixes(self.screen_pixes[x+(self.w)//2,y+(self.h)//2],self.target_pixes[self.w//2,self.h//2])
                if left_top and right_top and left_buttom and right_buttom and center:


                    if self.match(x,y,0.8):
                        print("找到了")
                        x = x + self.w//2
                        y = y + self.h//2
                        time.sleep(3)
                        self.mouse.click(x,y)
                        return 1

        print("没有找到")




if __name__ == '__main__':
    image = ImageMatch()
    # image.match()
    time.sleep(2)
    image.find_image("3.png")
