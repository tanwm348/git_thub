from woniu_atm.mysql import *
from woniu_atm.登陆 import login
class Person:
    def __init__(self,usname,pwd):
        self.usname = usname
        self.pwd = pwd
        sql = ("select * from woniu_atm where username ='%s'"%(usname))
        select(sql)

    def register(self):
        newname = input("请输入用户名：")
        newpwd = input("请输入密码：")
        if len(self.usname)>0:
            print("该用户已被注册，请重新输入新用户名！")
            self.register()
        else:
            sql7 = "insert into woniu_atm(username,passwd,money,num)values('%s','%s',%d,%d)"%(newname,newpwd,0,0)
            change_mysql(sql7)
            print("注册成功")



    def login(self,uname,pwd):
            uname = input("请输入用户名：")
            pwd = input("请输入密码：")
            if self.usname[0][0]==uname:
                if pwd == self.usname[0][1]:
                    print("登录成功！")
                else:
                     print("密码输入错误，请重新输入！")

def Ui(): # 定义主函数
            user = Person(usname="1",pwd="2") # 创建user对象
            print("=================================================================")
            print("=======================欢迎使用蜗牛atm取款机======================")
            print("=================================================================")
            print()
            print("请选择需要的操作:1.登陆 2.注册 3.解锁 4.注销 5.忘记密码 6.退出 ")
            on = input("请选择您需要进行的操作：")
            if on == "1":
                  login()
            elif on == "1":
                user.register
            else:
                print("输入有误，请重新输入！")


Ui()










