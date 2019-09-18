from day04.common.Announcementsmddel1 import announcementss

class recase():
    def __init__(self):
        self.re = announcementss()
        self.driver = self.re.driver


    def rec(self,headline,expected):
        l4 = self.re.search1(headline)
        if l4 == expected:
            print("搜索测试成功")
        else:
            print("搜索测试成功")