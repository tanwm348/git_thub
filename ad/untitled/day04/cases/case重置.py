from day04.common.Announcementsmddel1 import announcementss
class czcase():
    def __init__(self):
        self.c = announcementss()
        self.driver = self.c.driver



    def cz11(self,expected):
        l5 = self.c.cz()
        print(l5)
        print(expected)
        if l5 == expected:
            print("重置测试成功")
        else:
            print("重置测试失败")

