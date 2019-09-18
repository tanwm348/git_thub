from woniu_atm.mysql import *


class Person():
    def __init__(self,name,pwd,money):
        self.name = name
        self.pwd = pwd
        self.momey = money

    #查询余额
    def se(self):
        return self.momey

    def balance(self):
        num = input("请输入金额")
        if  self.momey>=num:
            self.momey = self.momey-num
            sql12 = "update woniu_atm set money = %d where username = '%s'"%(self.momey,self.name)
            change_mysql(sql12)
            print("'%s'当前余额为%d"%(self.name,self.momey))
            return self.momey
        else:
            return "余额不足"

    # def saveMoney(self):
