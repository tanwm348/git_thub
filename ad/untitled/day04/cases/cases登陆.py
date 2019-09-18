
from day04.common.loginmodel import *

#登陆测试
class logincase():
    def __init__(self):
     self.lon = login2()
     self.driver = self.lon.driver

    def login(self,username,password,expected):
      l1 = self.lon.logining(username,password)
      print(l1)
      if l1 == expected:
        print("测试成功")
      else:
        print("测试失败")
