from woniu_atm.mysql import *
def reg():

    newname = input("请输入你要注册的用户名")
    newpsd = input("请输入密码")
    sql6 = "select * from woniu_atm where username = '%s'"%(newname)
    aa = select(sql6)
    if len(aa) > 0:
        print("该用户已存在")
    else:
        sql7 = "insert into woniu_atm(username,passwd,money,num)values('%s','%s',%d,%d)"%(newname,newpsd,0,0)
        zc = change_mysql(sql7)
        print("注册成功")
        return zc
