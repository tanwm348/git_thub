from woniu_atm.mysql import *
def unlock():
    unname = input("请输入解锁账号")
    unpwd = input("请输入密码")
    sql17 = "select*from woniu_atm where username='%s'"%(unname)
    unk = select(sql17)
    if len(unk)<1:
        print("该用户不存在")
    elif  unk[0][1] == unpwd:
        sql18 = "select num from woniu_atm where username = '%s'"%(unname)
        num = select(sql18)
        num1 = num[0][0]-num[0][0]
        sql19 = "update woniu_atm set num = %d where username = '%s'"%(num1,unname)
        change_mysql(sql19)
        print("解锁成功")

