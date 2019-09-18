from day04.common.Announcementsmddel1 import announcementss

class comcase():
    def __init__(self):
        self.com = announcementss()
        self.driver = self.com.driver


    def com1(self,creator,headline,content,expected):
         l3 = self.com.compi(creator,headline,content)
         print(l3)
         if l3 == expected:
             print("编辑测试成功")
         else:
             print("编辑测试失败")






