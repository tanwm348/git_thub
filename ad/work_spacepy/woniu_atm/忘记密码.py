from woniu_atm.mysql import *
def forgetPassword():
 while True:
     uname = input("请输入账号")
     sql = "select*from woniu_atm where username = '%s'"%(uname)
     aa = select(sql)
     if len(aa)<1:
         print("该用户不存在")
     else:
         fpwd = int(input("请发送短信到110"))
         if fpwd == 1:
             fpwd1 = input("请输入新密码")
             fpwd2 = input("请再次输入密码")
             if fpwd1==fpwd2:
                sql3 = "update woniu_atm set passwd='%s' where username = '%s'"%(fpwd1,uname)
                change_mysql(sql3)
                print("密码修改成功")
                break
             else:
                 print("两次密码输入不一致")

         else:
             print("输入错误,请重新输入")

