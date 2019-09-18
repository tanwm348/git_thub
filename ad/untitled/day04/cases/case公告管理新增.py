from day04.common.Announcementsmddel1 import *

class anncases():
    def __init__(self):
     self.ann = announcementss()
     self.driver = self.ann.driver


    def addcase1(self,num,creator,headline,content,expected):
         l2 = self.ann.add(num,creator,headline,content)
         print(l2)
         if l2 == expected:
             print("新增测试成功")
         else:
             print("测试失败")

