from woniu_atm.mysql import *
def delee():
    dname = input("请输入注销账号")
    dpwd = input("请输入密码")
    sql19 = "select*from woniu_atm where username='%s'"%(dname)
    dele = select(sql19)
    if len(dele)<1:
        print("该用户不存在")
    elif  dele[0][1] == dpwd:
        sq20 = "delete from woniu_atm where username = '%s'"%(dname)
        change_mysql(sq20)
        print("'%s'注销成功"%(dname))

