import os


import cv2 as cv
from PIL import ImageGrab

class ImageMathOpenCV():
     def __init__(self,similarty):
        self.similarty = similarty

     def match_opencv(self,png):

         #大图路径
         basefoder = os.path.abspath(".")+"//screen//"
         #模板图片路径
         basefoder_tmp = os.path.abspath(".")+"//screen//"
         #截取大图
         ImageGrab.grab().save(basefoder+"image.png")


         #打开大图
         screen = cv.imread(basefoder+"image.png")

         #打开模板图片
         # temlate = cv.imread(basefoder_tmp+"3.png")
         temlate = cv.imread(basefoder_tmp+png)

         #开始匹配
         #参数   参数1:截图(大图);   参数2:模板图片(小图);  参数3:选择的匹配的算法
         # cv.TM_CCOEFF_NORMED---相关系数算法
         # 如果使用TM_CCOEFF_NORMED算法  返回的是一个相关系数矩阵  需要用minMaxLoc()函数来处理
         result = cv.matchTemplate(screen,temlate,cv.TM_CCOEFF_NORMED)
         # print(result)
         # 返回minVal,maxVal,minLoc,MaxLoc 4个值,分别是最小匹配度,最大匹配度,最小匹配度坐标,最大匹配度坐标
         minVal,maxVal,minLoc,maxLocs = cv.minMaxLoc(result)


         #匹配度
         simi = maxVal

         #要寻找的坐标   左上角顶点
         # print(maxLocs,type(maxLocs))
         x,y = maxLocs

         #获取模板图片的大小,用来寻找坐标中心点,返回宽高
         t = temlate.shape
         h,w = t[0:2]

         #计算中心点
         position_x = x+w//2
         position_y = y+h//2
         # print(simi)
         if simi>=self.similarty:
             print("找到了")
             return position_x,position_y
         else:
             return -1,-1




     # def login(self):
     #     mouse = PyMouse()
     #     keyboard = PyKeyboard()
     #
     #     x,y = self.match_opencv()
     #     mouse.click(x,y)
     #     keyboard.type_string("java")
     #













if __name__ == '__main__':
    pass
        # im = ImageMathOpenCV(0.8)
        # im.match_opencv()
        # im.login()
