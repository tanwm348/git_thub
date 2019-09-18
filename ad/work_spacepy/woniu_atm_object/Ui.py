from woniu_atm_object.person import Person
from woniu_atm_object.登陆 import login

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
                 Person.balance(money)
                # 取钱
                elif num2 == "2":
                  pass
                # 转账
                elif num2 == "3":
                    pass
                   # get = getmoney(log)
                # 查询余额
                elif num2 == "4":
                  money = log.balance()
                  print("当前余额为"+money)
                # 退出
                elif num2 == "5":
                    break
                elif num2 == "6":
                    pass
                    # vip(log)
                else :
                   print("输入有误")
        # 注册
        elif num == "2":
            pass
            # reg()
        elif num == "3":
        # 解锁
           pass
           # unlock()
        # 注销
        elif num == "4":
           pass
           # delee()
        # 忘记密码
        elif num == "5":
            pass
          # forgetPassword()
        # 退出
        elif num == "6":
            break
        else:
          print("操作有误")

ui()