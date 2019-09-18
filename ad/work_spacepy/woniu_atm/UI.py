from woniu_atm.登陆 import login
from woniu_atm.注册 import reg
from woniu_atm.查询余额 import balance
from woniu_atm.存钱 import savemaney
from woniu_atm.取钱 import drawmoney
from woniu_atm.转账 import getmoney
from woniu_atm.解锁 import unlock
from woniu_atm.注销 import delee
from woniu_atm.忘记密码 import forgetPassword
from woniu_atm.老板 import vip
def ui():

 while True:
        print("=================================================================")
        print("=======================欢迎使用蜗牛atm取款机======================")
        print("=================================================================")
        print()
        print("请选择需要的操作:1.登陆 2.注册 3.解锁 4.注销 5.忘记密码 6.退出 ")
        num = input("请选择你的操作")
        # 登陆
        if num == "1":
            log = login()
            if log == True:
               continue

            if log != 0:
              while True:
                num2 = input("请选择你的操作1.存钱,2.取钱,3.转账,4.查询余额,5退出,6.vip")
                # 存钱
                if num2 == "1":
                   sa = savemaney(log)
                # 取钱
                elif num2 == "2":
                   dra = drawmoney(log)
                # 转账
                elif num2 == "3":
                   get = getmoney(log)
                # 查询余额
                elif num2 == "4":
                   ba = balance(log)
                # 退出
                elif num2 == "5":
                    break
                elif num2 == "6":
                    vip(log)
                else :
                   print("输入有误")
        # 注册
        elif num == "2":
            reg()
        elif num == "3":
        # 解锁
           unlock()
        # 注销
        elif num == "4":
           delee()
        # 忘记密码
        elif num == "5":
          forgetPassword()
        # 退出
        elif num == "6":
            break
        else:
            print("操作有误")

ui()