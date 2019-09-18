from day04.common.Announcementsmddel1 import announcementss
class decase():
    def __init__(self):
        self.d = announcementss()
        self.driver = self.d.driver



    def dete(self,expected):

        l6 = self.d.dele()
        print(l6)

        if l6 == expected:
            print("删除测试成功")
        else:
            print("删除测试失败")
